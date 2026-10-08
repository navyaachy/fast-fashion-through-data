##### \# Fast Fashion Through Data

##### 

##### \## Analysing Material Composition, Sustainability and Product Pricing

##### 

##### \---

##### 

##### \## Problem Statement

##### 

##### Fast fashion increasingly incorporates synthetic and recycled materials while presenting sustainability-related information at the product level. However, it is difficult to identify broader patterns in material composition, sustainability indicators and product pricing across a large product catalogue.

##### 

##### This project analyses H\&M product data to examine material usage, identify recycled-material indicators, and investigate how these factors are associated with retail pricing and product categories.

##### 

##### \---

##### 

##### \## Objectives

##### 

##### The project aims to:

##### 

##### \- Analyse the distribution of H\&M product prices.

##### \- Identify the most commonly mentioned materials in product compositions.

##### \- Identify products containing recycled-material indicators.

##### \- Compare the average prices of products with and without recycled-material mentions.

##### \- Analyse product categories and their pricing patterns.

##### \- Compare average prices across broader category groups.

##### \- Identify data-driven patterns in H\&M's product catalogue.

##### 

##### \---

##### 

##### \## Dataset

##### 

##### The project uses the H\&M Product Dataset available on Kaggle.

##### 

##### \*\*Dataset Source:\*\*  

##### https://www.kaggle.com/datasets/niharpatel03/h-and-m-product-dataset

##### 

##### The dataset contains product-level information including:

##### 

##### \- Product ID

##### \- Product name

##### \- Brand name

##### \- Price

##### \- Stock state

##### \- Colour information

##### \- Product category

##### \- Product details

##### \- Material composition

##### 

##### The raw dataset is not stored in this repository because it is third-party data and is approximately 19 MB in size.

##### 

##### \---

##### 

##### \## Project Workflow

##### 

##### H\&M Product Dataset

##### &#x20;       ↓

##### Data Loading

##### &#x20;       ↓

##### Basic Data Inspection \& Cleaning

##### &#x20;       ↓

##### Material Composition Extraction

##### &#x20;       ↓

##### Material Frequency Analysis

##### &#x20;       ↓

##### Recycled-Material Indicator

##### &#x20;       ↓

##### Product Category Analysis

##### &#x20;       ↓

##### Price Analysis

##### &#x20;       ↓

##### Visualisation

##### &#x20;       ↓

##### Data-Driven Findings

##### 

##### \---

##### 

##### \## Analysis Performed

##### 

##### \### 1. Dataset Overview

##### 

##### The dataset was inspected to understand:

##### 

##### \- Number of records

##### \- Available columns

##### \- Missing values

##### \- Price statistics

##### \- Product and category information

##### 

##### \### 2. Price Analysis

##### 

##### The distribution of product prices was analysed to understand the overall pricing pattern of products in the dataset.

##### 

##### \### 3. Material Composition Analysis

##### 

##### The material information provided in the product descriptions was processed to extract material names and their percentage composition.

##### 

##### The frequency of commonly mentioned materials was then analysed.

##### 

##### \### 4. Recycled-Material Analysis

##### 

##### A sustainability indicator was created by identifying whether the product's material information contains a recycled-material mention.

##### 

##### Products were then compared based on whether a recycled-material mention was present.

##### 

##### \### 5. Price Comparison

##### 

##### The average listed price was compared between products with a recycled-material mention and products without a recycled-material mention.

##### 

##### This analysis identifies an association in the dataset and does not imply that recycled materials directly cause higher prices.

##### 

##### \### 6. Category Analysis

##### 

##### Product categories were analysed to identify the most represented product groups.

##### 

##### Average prices were also compared across product categories and broader category groups.

##### 

##### \---

##### 

##### \## Key Findings

##### 

##### The initial analysis identified the following patterns:

##### 

##### \- Polyester, cotton and spandex are among the most frequently mentioned materials.

##### \- Around \*\*60.65%\*\* of the product records contain a recycled-material mention.

##### \- Products with a recycled-material mention have a higher average listed price than products without one in this dataset.

##### \- Product categories differ considerably in both product count and average listed price.

##### \- Among the identified category groups, sportswear has the highest average listed price, followed by men's and ladies' products.

##### 

##### These findings describe patterns and associations within the dataset and should not be interpreted as causal relationships.

##### 

##### \---

##### 

##### \## Technologies and Open-Source Tools

##### 

##### The project uses:

##### 

##### \- \*\*Python\*\* for data analysis

##### \- \*\*Pandas\*\* for data processing and analysis

##### \- \*\*Matplotlib\*\* for data visualisation

##### \- \*\*Jupyter Notebook / Google Colab\*\* for analysis

##### \- \*\*Git\*\* for version control

##### \- \*\*GitHub\*\* for repository management and collaboration

##### \- \*\*Docker\*\* for reproducible execution and environment management

##### 

##### \---

##### 

##### \## Repository Structure

##### 

##### The repository is organised into the following structure:

##### 

##### \- `data/` contains raw and processed data

##### \- `notebooks/` contains the data-analysis notebook

##### \- `outputs/` contains generated outputs and visualisations

##### \- `src/` contains reusable source code

##### \- `.gitignore` prevents raw data and temporary files from being committed

##### \- `README.md` contains project documentation

##### \- `LICENSE` contains the project license

##### \- `requirements.txt` contains Python dependencies

##### \- `Dockerfile` contains the container configuration

##### \- `docker-compose.yml` contains the Docker Compose workflow

##### 

##### \---

##### 

##### \## Reproducibility

##### 

##### The project is structured to support reproducible analysis using:

##### 

##### \- Git and GitHub for version control

##### \- A requirements file for Python dependencies

##### \- Docker for environment consistency

##### \- Documented project workflow and setup instructions

##### 

##### The raw dataset is excluded from version control because it is third-party data and is approximately 19 MB in size.

##### 

##### To reproduce the analysis, obtain the dataset from the original Kaggle source and place it in the appropriate local data directory before running the project.

##### 

##### \---

##### 

##### \## Version Control

##### 

##### Git and GitHub are used to manage the project and track development.

##### 

##### The repository demonstrates:

##### 

##### \- Version-controlled project files

##### \- Meaningful commits

##### \- Feature branching

##### \- Branch merging

##### \- Remote GitHub repository management

##### 

##### \---

##### 

##### \## Sustainability Analysis Note

##### 

##### The recycled-material indicator is based on the presence of recycled-material information in the product's material description.

##### 

##### Therefore, the analysis measures the \*\*presence of a recycled-material mention\*\*, rather than independently verifying the sustainability or environmental impact of the product.

##### 

##### \---

##### 

##### \## Limitations

##### 

##### \- The analysis is based on the available H\&M product dataset.

##### \- Material information is derived from product descriptions.

##### \- The presence of a recycled-material mention does not measure the complete environmental impact of the product.

##### \- Price comparisons show associations and do not establish causation.

##### \- Category groups are derived from the available product category codes.

##### 

##### \---

##### 

##### \## Future Scope

##### 

##### The project can be extended by:

##### 

##### \- Analysing more detailed sustainability indicators.

##### \- Exploring relationships between material composition and product categories.

##### \- Expanding the analysis to additional product attributes.

##### \- Automating the data-processing and analysis pipeline.

##### \- Improving reproducibility through containerisation.

##### 

##### \---

##### 

##### \## License

##### 

##### The original code and documentation developed for this project are licensed under the \*\*MIT License\*\*.

##### 

##### The H\&M product dataset is third-party data and remains subject to its original source terms and licensing.

##### 

##### See the `LICENSE` file for the project license.

