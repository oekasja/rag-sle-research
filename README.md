# Specialized Medical RAG-based LLM Dataset (SLE Case Study)

This repository serves as a complete artifact for reproducing, evaluating, and extending the research findings presented in the paper:

**"Impact of Knowledge Source Type on RAG-Based LLMs in Specialized Medical Domains: A Case Study on Systemic Lupus Erythematosus"**
*Soon Published in: IEEE* (Full Citation below)

## Overview

This repository provides all essential components used to study the performance of a medical Retrieval-Augmented Generation (RAG) system for a specialized condition, specifically Systemic Lupus Erythematosus (SLE). This includes:

1.  **Metadata of Knowledge Sources:** Curated lists of documents.
2.  **Evaluation Data:** Question bank and raw expert scores.
3.  **Experimental Artifacts:** Technical configurations and system setup files.
4.  **Analysis Tools:** Python scripts for statistical evaluation.

## Repository Structure & File Descriptions

Here is a detailed breakdown of the contents of this repository:

| File / Directory | Description | Type |
| :--- | :--- | :--- |
| `README.md` | This file. Provides project overview and instructions. | Documentation |
| **Data & Metadata** | | |
| `list_of_med_docs.md` | Metadata of the 28 medical documents used as the RAG knowledge base. Organized by source type (Textbooks, Journal Articles, Clinical Practice Guidelines). Includes titles, authors, and years. | Dataset Metadata |
| `question_bank.md` | The comprehensive set of 45 medical queries (questions) designed to test the RAG system's capabilities for SLE case management. | Evaluation Dataset |
| `scoring_results.csv` | Anonymized raw evaluation scores provided by three independent medical experts. Contains columns for: `Question_ID`, `Answer_ID`, `Source_Type`, and scores from `Expert_1`, `Expert_2`, `Expert_3`. | Raw Dataset |
| **System Artifacts** | | |
| `dify-setup-sle-rag-research.yml` | Full configuration file to recreate the specific application setup used in this research within the [Dify](https://github.com/langgenius/dify) platform. This includes workflow definitions, prompt templates, and UI settings. *Note: Data and credentials are not included.* | System Config |
| `system_config.json` | Key technical hyperparameters and metadata for the RAG pipeline components (e.g., embedding model used, chunk size, retrieval method). This complements the Dify setup file. | System Config |
| **Analysis Tools (Scripts)** | | |
| `scoring_analysis.py` | Python script to perform basic descriptive statistics and analysis on the `scoring_results.csv` data (e.g., calculating average scores per category, identifying score distributions). | Python Script |
| `gwets_ac2_reliability_test.py` | Special-purpose Python script to calculate the Gwet's AC2 inter-rater reliability coefficient among the three medical experts, providing a measure of assessment consistency. | Python Script |

## Experts Profile

The expert evaluation was conducted by a panel of **three Internal Medicine Residents**.

These experts are currently in the **Internal Medicine Residency Program** at **Brawijaya University, Indonesia**. They have specific training and experience in diagnosing and managing complex cases of SLE.

## Reproduction & Usage

1.  **Understand the Methodology:** Review the detailed breakdown of medical documents (`list_of_med_docs.md`) and the specific questions used (`question_bank.md`).
2.  **Inspect the Configuration:** Check `system_config.json` to understand the technical parameters and use `dify-setup-sle-rag-research.yml` if you wish to replicate the application environment within the [Dify](https://github.com/langgenius/dify) platform.
3.  **Run Analysis:** Execute the provided Python scripts to reproduce the statistical analysis:
    * To calculate basic statistics: `python scoring_analysis.py`
    * To measure expert agreement: `python gwets_ac2_reliability_test.py`

## Citation

If you use this dataset, artifacts, or analysis methods in your research, please cite our official paper:

> **[FULL PAPER AUTHORS], "Impact of Knowledge Source Type on RAG-Based LLMs in Specialized Medical Domains: A Case Study on Systemic Lupus Erythematosus", *IEEE [Conference/Journal Title]*, [Vol/Issue, Pages, Date].**
> *(We will replace with the final citation data once published)*

### Abstract

Factual reliability remains a critical bottleneck for Large Language Models (LLMs) in specialized medical domains like Systemic Lupus Erythematosus (SLE). While Retrieval-Augmented Generation (RAG) mitigates hallucinations, the qualitative impact of different underlying knowledge sources remains under-explored. This paper addresses this gap by evaluating three distinct repositories—Medical Textbooks, Academic Journals, and Clinical Guidelines—within a multi-path RAG framework using an open-weights, small-scale LLM (Gemma-3:4b). Based on a double-blind assessment of 45 stratified queries by three medical residents, we map the unique competency profiles of each source type. The core contributions of this study are twofold: (1) we provide an empirical characterization of medical source trade-offs, demonstrating that textbooks excel in foundational clarity and complex reasoning, guidelines ensure procedural precision, and journals provide technical depth at the cost of synthesis friction; and (2) we offer initial empirical insights that can help the development of future intent-aware RAG routing mechanisms to enhance clinical safety.

## Contact

For questions regarding the dataset, code, or paper, please contact:
*   [oekasja@gmail.com](mailto:oekasja@gmail.com)
*   [ukasyazr@student.telkomuniversity.ac.id](mailto:ukasyazr@student.telkomuniversity.ac.id)
