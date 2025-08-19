# Multifunctional ETL Pipeline: Heterogeneous Data Consolidation

This repository contains a Python script (`etl_code.py`) designed to perform a comprehensive Extract, Transform, Load (ETL) process for data from multiple sources.

## Purpose for Recruiters

This script showcases my ability to build **robust and automated data processing solutions** that can be integrated into larger data workflows. It demonstrates my proficiency in handling data extraction from **various formats** (CSV, JSON, XML), performing critical data transformations, and effectively loading the results.

**Demonstrated Skills:**
* **Data Engineering:** Design and implementation of data pipelines.
* **Heterogeneous Data Handling:** Ability to work with diverse data formats (CSV, JSON, XML).
* **Data Processing:** Skill in cleaning, structuring, and preparing data for analysis or storage.
* **Automation:** Creation of scripts that can be executed programmatically or on demand.
* **ETL Fundamentals:** Practical understanding of the Extract, Transform, Load phases.
* **Key Library Usage:** Familiarity with essential libraries for data manipulation and processing.

## Description

The `etl_code.py` file encapsulates the logic for:
1.  **Extraction (Extract):** [Describe here where the data is extracted from, e.g., a SQL database, CSV files, an API, etc. Based on the code snippet, it extracts from CSV, JSON, and XML files within the directory.]
2.  **Transformation (Transform):** [Detail the data cleaning, enrichment, or restructuring operations performed, e.g., filtering, aggregation, joins, calculation of new columns, handling of null values, etc. The code snippet shows height/weight conversion.]
3.  **Loading (Load):** [Explain where the transformed data is loaded, e.g., another database, an output file, a data warehouse, etc. The code snippet shows loading to a CSV file.]

## Requirements

To run this script, you will need Python (preferably Python 3.x) and the following libraries. You can install them using pip:

```bash
pip install pandas lxml # `lxml` is often needed for robust XML parsing; `glob` and `datetime` are built-in.