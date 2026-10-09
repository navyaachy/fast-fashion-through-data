# FashionLens: Fast Fashion Through Data

**Analysing Material Composition, Sustainability and Product Pricing**

## 1. Project Overview

FashionLens is a data analysis project that explores H&M product data to identify patterns in material composition, sustainability-related indicators and retail pricing. It uses Python, Pandas and Matplotlib to process product information and generate visual insights.

The project also demonstrates open-source development practices through Git, GitHub, Docker and Docker Compose.

## 2. Problem Statement

Fast fashion products contain different materials and may include sustainability-related information, such as recycled-material mentions. Identifying patterns across a large product catalogue can be difficult when examining products individually.

FashionLens analyses H&M product data to understand commonly used materials, identify recycled-material mentions and examine how pricing varies across products and categories.

## 3. Objectives

- Analyse the distribution of product prices.
- Identify commonly mentioned materials in product descriptions.
- Examine the frequency of recycled-material mentions.
- Compare average prices between products with and without recycled-material mentions.
- Explore pricing differences across product category groups.
- Build a reproducible analysis pipeline using open-source tools.

## 4. Dataset

**Dataset:** H&M Product Dataset  
**Source:** https://www.kaggle.com/datasets/niharpatel03/h-and-m-product-dataset  
**File used:** `handm.csv`

The dataset contains 9,677 product records and 16 columns, including product identifiers, product names, prices, category codes, material descriptions and colour information.

The original dataset is subject to the terms and conditions of its source.

## 5. Technology Stack

- **Python:** Data processing and analysis.
- **Pandas:** Data cleaning, transformation and aggregation.
- **Matplotlib:** Data visualization.
- **Regular Expressions (Regex):** Extracting material information from text.
- **Google Colab:** Exploratory analysis and notebook execution.
- **Git:** Version control.
- **GitHub:** Source-code hosting and repository management.
- **Docker:** Containerizing the analysis environment.
- **Docker Compose:** Building and running the analysis pipeline.

## 6. Project Workflow

1. Load the H&M product dataset.
2. Inspect the dataset structure and missing values.
3. Analyse product price distributions.
4. Extract material names from product descriptions.
5. Count frequently mentioned materials.
6. Identify products containing recycled-material mentions.
7. Compare average prices between the two groups.
8. Analyse average prices across selected product category groups.
9. Generate visualizations and summary outputs.
10. Run the analysis through a Docker Compose workflow.

## 7. Key Findings

The analysis produced the following initial findings:

- The dataset contains **9,677 product records**.
- **5,869 records (60.65%)** contain a recycled-material mention in the materials field.
- Products with a recycled-material mention have an average listed price of approximately **35.55**, compared with **32.16** for products without such a mention.
- Polyester, cotton and spandex are among the most frequently extracted material mentions.
- Among the selected category groups, sportswear has the highest average listed price, followed by men's products and ladies' products.

These findings describe associations and patterns in the dataset. They do not establish that recycled materials cause higher prices or independently verify a product's environmental impact.

## 8. Repository Structure

```text
fast-fashion-through-data/
├── notebooks/
├── outputs/
├── src/
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── README.md
└── requirements.txt
```

The raw dataset is excluded from version control and must be downloaded separately.

## 9. Installation and Execution

**Prerequisites**

- Python
- Git
- Docker Desktop with Docker Compose
- The H&M dataset saved as `data/raw/handm.csv`

**Run using Docker Compose**

Clone the repository and enter its directory. Download the dataset and place it at the required path, creating the `data/raw/` folders if necessary.

Then execute:

```bash
docker compose up --build
```

The pipeline processes the dataset and generates analysis outputs in the `outputs/` directory.

**Run using Python**

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis script:

```bash
python src/analyze.py
```

Ensure that the dataset is available at the expected path before execution.

## 10. Version Control

The project uses Git and GitHub to track changes and maintain the source code.

The repository includes a `main` branch and a `feature/reproducibility` branch. The feature branch was integrated into `main` through a fast-forward merge.

The `.gitignore` file excludes the raw dataset, Python cache files and Jupyter checkpoint files.

## 11. Reproducibility

The project includes a requirements file, a Dockerfile and a Docker Compose configuration to document dependencies and provide a consistent execution environment.

Users must download the dataset separately because the raw CSV is not stored in the repository. The dataset should be saved using the expected filename and directory structure.

## 12. Limitations

- The analysis uses a single H&M product dataset.
- The presence of the word “Recycled” is used as an indicator, not as independent verification of sustainability.
- Missing material descriptions may affect the recycled-material comparison.
- Material counts represent extracted mentions, not necessarily unique products.
- Price comparisons are descriptive and do not establish causation.
- The project does not train a machine learning model or provide price predictions.
- The current repository contains a notebook and analysis pipeline rather than a deployed web application.

## 13. Future Scope

Potential extensions include improved material extraction, more detailed category comparisons, statistical testing of price differences and integration of independently verified sustainability information.

## 14. License

The project's original code and documentation are distributed under the MIT License. Third-party datasets remain subject to their respective source terms.

## 15. Conclusion

FashionLens demonstrates how open-source data analysis tools can be used to investigate material composition, recycled-material mentions and pricing patterns in fast fashion. The project combines exploratory data analysis with Git-based version control and containerized execution to create a documented and reusable workflow.
