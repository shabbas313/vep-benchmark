import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_auc_score

#1. Data Loading and Configuration

try:
    df = pd.read_csv('2024_ClinVar.csv') 
except FileNotFoundError:
    print("Error: '2024_ClinVar.csv' not found.")
    exit()
# Defining Selected Models for AF Comparsion
MODELS_TO_ANALYZE = {
    'MetaRNN_score': 'MetaRNN',
    'BayesDel_addAF_score': 'BayesDel_addAF',
    'ClinPred': 'ClinPred',
    'REVEL': 'REVEL',
    'gMVP_score': 'gMVP',
    'AlphaMissense_score': 'AlphaMissense'
}

# True label column [1=Pathogenic, 0=Benign]
TRUE_LABEL_COL = 'clinvar_label' 
AF_COL = 'gnomADg_AF'

# 2. Data Preparation
required_cols = list(MODELS_TO_ANALYZE.keys()) + [TRUE_LABEL_COL, AF_COL]
if not all(col in df.columns for col in required_cols):
    print(f"Error: Missing one or more required columns in the CSV. Needed: {required_cols}")
    exit()

# Handle missing Allele Frequencies: treat them as 0
df[AF_COL] = df[AF_COL].fillna(0)
# Ensure the AF column is numeric
df[AF_COL] = pd.to_numeric(df[AF_COL], errors='coerce').fillna(0)


# Define the binning function
def assign_af_bin(af):
    if af == 0:
        return 'AF = 0 (Singletons)'
    elif 0 < af <= 0.00001:
        return '0 < AF <= 1e-5'
    elif 0.00001 < af <= 0.0001:
        return '1e-5 < AF <= 1e-4'
    elif 0.0001 < af <= 0.001:
        return '1e-4 < AF <= 1e-3'
    else:
        return 'AF > 1e-3'

df['AF_Bin'] = df[AF_COL].apply(assign_af_bin)

bin_order = [
    'AF = 0 (Singletons)',
    '0 < AF <= 1e-5',
    '1e-5 < AF <= 1e-4',
    '1e-4 < AF <= 1e-3',
    'AF > 1e-3'
]


# 3. Iterate and Calculate Metrics 
results = []
print("Calculating AU-ROC for each model in each AF bin...")

for bin_name in bin_order:
    bin_df = df[df['AF_Bin'] == bin_name]
    
    if len(bin_df) < 10 or len(bin_df[TRUE_LABEL_COL].unique()) < 2:
        print(f"Skipping bin '{bin_name}' due to insufficient data or only one class present.")
        continue
        
    for score_col, model_name in MODELS_TO_ANALYZE.items():
        subset = bin_df[[TRUE_LABEL_COL, score_col]].dropna()
        
        if len(subset) < 10 or len(subset[TRUE_LABEL_COL].unique()) < 2:
            continue

        y_true = subset[TRUE_LABEL_COL]
        y_pred = subset[score_col]
        
        auc = roc_auc_score(y_true, y_pred)
        
        results.append({
            'Model': model_name,
            'AF_Bin': bin_name,
            'AU-ROC': auc,
            'Variant_Count': len(subset)
        })

results_df = pd.DataFrame(results)

print("\nCalculation complete. Plotting results...")
print(results_df)


# 4. Plot the Results 
plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid", rc={"grid.linestyle": "--"})

custom_palette = {
    'MetaRNN': 'mediumblue',        
    'BayesDel_addAF': 'dodgerblue', 
    'ClinPred': '#006D5B',          
    'REVEL': 'lime',                
    'gMVP': '#827717',              
    'AlphaMissense': '#003087'
}

lineplot = sns.lineplot(
    data=results_df,
    x='AF_Bin',
    y='AU-ROC',
    hue='Model',
    style='Model',         
    markers=True,           
    markersize=12,         
    linewidth=3,            
    palette=custom_palette, 
    hue_order=list(custom_palette.keys())
)

#plt.title('Model Performance by Allele Frequency Bin', fontsize=24, pad=20, weight='bold')
plt.xlabel('Allele Frequency Bin (gnomAD)', fontsize=12, labelpad=15)
plt.ylabel('AU-ROC', fontsize=12)
plt.xticks(rotation=15, ha='right', fontsize=14)
plt.yticks(np.arange(0.5, 1.05, 0.1), fontsize=14) 
plt.ylim(0.5, 1.02)
plt.legend(
    title='Model', 
    fontsize=11, 
    title_fontsize=12, 
    bbox_to_anchor=(1.02, 0.5), 
    loc='center left'           
)
plt.tight_layout(rect=[0, 0, 0.85, 1]) 

bin_counts = results_df.groupby('AF_Bin')['Variant_Count'].mean().reindex(bin_order)
for i, count in enumerate(bin_counts):
    if not pd.isna(count):
      plt.text(i, 0.51, f'n ≈ {int(count)}', ha='center', color='black', fontsize=12, style='italic')

plt.tight_layout()
plt.savefig('Performance_vs_Allele_Frequency.png', dpi=300)
#plt.savefig('Performance_vs_Allele_Frequency.svg')
plt.show()