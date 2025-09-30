# Evaluating the Performance of Variant Effect Predictors: A Comprehensive Analysis Utilizing Clinical and High-throughput Functional Data

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository serves as a supplementary archive for our manuscript, "Evaluating the Performance of Variant Effect Predictors: A Comprehensive Analysis Utilizing Clinical and High-throughput Functional Data". It contains key scripts, results, and figures presented in the study.

In this study, we performed a rigorous, multifaceted performance validation of 29 widely used *in-silico* pathogenicity predictors. Our findings identify the most reliable predictors for clinical application but also uncover a significant disparity in model performance between clinical and functional benchmarks, providing a vital guide for the informed application of these powerful models in advanced genomic medicine. 

## Study Workflow
Here us the overall workflow of our study, from data curation to interpretation:

![Study Workflow Figure](results/figures/Fig_1.png)

## Repository Contents
This repository is organized as follows:
-   `code/`: Contains key analysis scripts for performance evaluation and figure generation.
-   `results/figures/`: Contains all figures presented in the manuscript in high-resolution format.
-   `results/tables/`: Contains supplementary tables with detailed performance metrics (e.g., MCC, AU-ROC) for all predictors.

## Key Results Showcase

Below are the key findings from our analysis.

## Figures Showcase

This section provides an overview of the key figures from our manuscript. All high-resolution figures are available in the `results/figures/` directory.

| Preview                                       | Figure Number & Title                                      | Description                                                                                             |
| :-------------------------------------------- | :--------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| ![Figure 1](results/figures/Fig_1.png)        | **Figure 1:** Overview of the study design for the comprehensive evaluation of in-silico pathogenicity predictors.	| The workflow invloves curating benchmark datasets from four primary sources (ClinVar, BRCA1/2 Clinicalset (gnomAD), BRCA2 functional study, and a disease-specific set from CFTR2). These datasets were used to evaluate the performance of 29 predcitoes, categorized by methodology, using metrics including AU-ROC, AUPRC, and MCC, followed by a comparative analysis             |
| ![Figure 2](results/figures/Fig_2.png) | **Figure 2:** Comparison of data completeness across 29 variant effect predictors using clinical data.                           | The bar plots show the percentage of missing prediction scores (A) Results on the primary ClinVar dataset (n=21,718 pathogenic; n=30,173 benign), where predictors such as EVE and MPC have the highest rates of missing values, exceeding 30%. (B) Results on ClinVar Independent dataset (n=756 benign; n=616 pathogenic). While the trend is similar, the overall percentage of missing values is lower for the most tools on this dataset.	|
| ![Figure 3](results/figures/Fig_3.png)        | **Figure 3:** Comparative ROC analysis of 29 selected models across clinical dataset. 	| AU-ROC curve of the primary dataset, sorted by performance, where MetaRNN (AUC=0.990) and ClinPred (AUC=0.986) show the highest accuracy. (B) AU-ROC curve for the balanced subset, showing ~ a similar hierarchy of highest performance with MetaRNN (AUC=0.984). (C) AU-ROC using an independent ClinVar dataset, where overall performance is lower, but MetaRNN 9AUC=0.973) and BayesDel_addAF (AUC=0.967) maintain a significant predictive advantage.             |
| ![Figure 4](results/figures/Fig_4.png)        | **Figure 4:** Comparative performance analysis by model category and evaluation dataset.	| Box and strip plot illustrating the distribution of AU-ROC scores for each model across the ClinVar datasets (Boxes are colored by model category, and individual points are colored by dataset, showing both overall performance and consistency). The tools are ranked, highlighting a clear performance hierarchy where met-predictors and integrated tools such as MetaRNN, BayesDel, and ClinPred consistently outperforms all other categories.             |
| ![Figure 5](results/figures/Fig_5.png)        | **Figure 5:** Evaluation of predictor performance at recommended thresholds and stratification by allele frequency. 	| Sensitivity versus specificity for each predictor at its recommended threshold on the (A) ClinVar primary dataset, (B) Clinvar balanced subset, and (C) Independent datasets. Top-tier meta-predictors consistently achieve high performance, clustering in the top-right corner. (D) AU-ROC performance of the top-performing models stratified by gnomAD allele frequency 9AF) bins. All models shows the highest AU-ROC on the rarest variants (singletons), with performance generally decreasing for more common variants, a known challenge in variant interpretation.              |
| ![Figure 6](results/figures/Fig_6.png)        | **Figure 6:** Comparative performance of the models on clinical genes versus functional (SGE) datasets.	| The performance of predictors was evaluated on a clinical genes datasets of BRCA1/BRCA2 variants sourced from gnomAD (clinical classification (pathogenic/benign) by ClinVar) and a high-throughput functional datasets from a saturation genome editing (SGE) experiments on BRCA2. (A) AU-ROC measures the overall ability to distinguish pathogenic from benign variants (B) Matthews correlation coefficient (MCC) evaluates classification accuracy at the tools recommended thresholds. Models are sorted in descending order on the basis of their performance on the SGE dataset. The drastic reduction in performance across all models on SGE dataset highlights the challenge of predicting functional impact compared with clinical pathogenicity. The dashed lines indicate the performance of a random classifier (AU-ROC = 0.5; MCC = 0).             |

## Benchmark Datasets 
Due to their large file size, the benchmark datasets analyzed in this study are not hosted on this GitHub repository. The full datasets are available from the author upon reasonable request.
  
**How to Request Data:**
To request access, please email [Syed Hassan Abbas] at [abbas.hassan@stu.ecnu.edu.cn] with a brief description of your intended research use. The datasets will be provided in `.csv` format. In all files, the ground truth labels are in a column named `Label` (1 = Pathogenic, 0 = Benign).

#### Dataset Descriptions:
-   **ClinVar Datasets:** Derived from the ClinVar database (accessed [Dec, 2024]). Includes a primary imbalanced set, a balanced subset, and a temporal validation set (variants submitted [Jan, 2025] to [May, 2025]) to ensure non-circularity.
-   **BRCA Clinical Dataset:** A gene-specific set of missense variants in *BRCA1* and *BRCA2*. Variants with high-confidence clinical classifications from ClinVar were retained and subsequently filtered to remove common variants found in gnomAD (AF > [1%]).
-   **BRCA2 SGE Functional Dataset:** A large-scale experimental dataset derived from a saturation genome editing study of *BRCA2* [1].
-   **CFTR2 Disease-Specific Dataset:** A high-confidence set of CF-causing and non-CF-causing variants from the CFTR2 database (https://cftr2.org/). 

## Citation
If you find our work useful, please cite our paper:
> **[Syed Hassan Abbas, et al. (Year). Evaluating the Performance of Variant Effect Predictors: A Comprehensive Analysis Utilizing Clinical and High-throughput Functional Data. *Journal Name*.]**


## Reference
1. Sahu S, Galloux M, Southon E, Caylor D, Sullivan T, Arnaudi M, et al. Saturation genome editing-based clinical classification of BRCA2 variants. Nature. 2025;638(8050):538-45.

## Contact 
For questions about the paper or data, please contact [Syed Hassan Abbas] at [abbas.hassan@stu.ecnu.edu.cn] or open an issue in this repository.