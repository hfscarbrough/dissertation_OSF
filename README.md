# Hannah Scarbrough's Dissertation GitHub Files

This repository contains the files related to analysis for ***From Meta-Analysis to Practice: Understanding How Education Research is Interpreted and Applied***

## Abstract

Meta-analysis is a powerful tool for summarizing research that policymakers and practitioners can use to make decisions in education contexts. A high-quality meta-analysis includes detailed reporting of each stage to increase transparency and reproducibility and mitigate researcher bias (Pigott & Polanin, 2020). This leads to highly detailed reports that can be difficult for a non-technical audience to interpret accurately or appropriately. Building on a previously conducted meta-review of quality and use of research evidence (URE) strategies in education meta-analyses (Pellegrini et al., 2025b), the proposed study explores the documents that cite meta-analytic research in practice contexts, the evidence they report, and how strategies employed by the meta-analysis to communicate evidence is associated with documents using the evidence. A sample of twenty meta-analyses in K-12 education were forward searched to identify 186 unique documents that contained 197 references to the meta-analyses in the sample. Documents within a practice context were coded for their goals and the content reported related to effects and contextual information. In general, documents were published by researchers (73%) in traditional research publications (33%) or informal blog-style posts (30%). Intervention effects were most often described (57%) and did not include specific statistics (74%). On average, each meta-analysis had 13.2 citing documents, with meta-analysis on reading having a higher average along with meta-analyses that included a section dedicated to policy and practice implications. In general, strategies aimed towards increasing the use of meta-analytic evidence by making the results more accessible to interest-holders did not lead to more citing documents. This suggests that the main strategies are not being used appropriately or are not as useful to interest-holders as researchers thought. Additionally, there is still some disconnect in the most relevant information a meta-analysis can offer interest-holders. Documents rarely reported the variations in effects of an intervention that tell us for whom and under what conditions an intervention works best. This study concludes with a discussion of the results within the context of bridging the gap between researchers and practice. Recommendations for researchers, limitations, and future directions are also discussed. 

# Contents of GitHub Repository

All files for analysis are written using Markdown and have a knitted HTML file of the output. 

## Folders

📁 **data** ~ Contains all .csv files for analysis

📁 **figures** ~ Files related to building tables in text

📁 **literature_searching** ~ Python code files and results for scraping Google results

📁 **maps** ~ Data files related to constructing maps

📁 **tables** ~ Files related to building tables in text

📁 **visuals** ~ Visualizations produced for text


## Files

### Codebook 1 Analysis

📄 **1a_included_ma_descriptives** ~ Descriptives of the 20 meta-analyses

📄 **1b_forward_results_all** ~ Results of Forward Search, building visuals for results

### Codebook 2 analysis

📄 **2a_cleaning** ~ Data cleaning steps for practice documents. **MUST** run before any files beginning with '3_'

📄 **3a_s2_visuals_analysis** ~ Includes visuals and simple analyses of the coded documents 

📄 **3b_s2_regression** ~ Code for regressions, correlations, and summary statistics of strategy on number of documents

📄 **3c_s2_es_accuracy** ~ Code for checking accuracy of reported effects 

📄 **3d_s2_examples** ~ Looks at documents citing example meta-analyses to compare to broader sample. Not included in manuscript

📄 **3e_s2_practice_languages** ~ List of countries and languages represented in practice documents.
