# Automotive Sales & Performance Analytics: Interactive Looker Studio Dashboard

LINK:
https://lookerstudio.google.com/reporting/631b7d22-9b04-47c8-ace6-9b26d7b82bc3

This project features an interactive dashboard developed in **Looker Studio** (formerly Google Data Studio) to analyze key metrics related to sales, profitability, car recalls, and customer sentiment within the automotive sector. The dashboard integrates and visualizes data from multiple sources, demonstrating the ability to transform raw data into actionable insights.

## Purpose for Recruiters

This project is direct evidence of my proficiency in **business intelligence (BI)** and **data visualization**. It demonstrates my ability to:
* **Design and build intuitive dashboards** that effectively communicate complex information.
* **Integrate multiple datasets** to create a unified view of business performance.
* **Translate business requirements into meaningful metrics and visualizations**.
* **Identify trends, patterns, and anomalies** in large volumes of data.
* **Utilize industry-leading BI tools** (Looker Studio), a highly in-demand skill.

It perfectly complements my ETL skills by showcasing the **final stage of the data pipeline**: delivering value through analysis and visualization.

**Demonstrated Skills:**
* **Business Intelligence (BI):** Report and dashboard design.
* **Data Visualization:** Creation of meaningful and aesthetically pleasing charts.
* **Data Analysis:** Extracting insights from sales, profitability, quality issues, and sentiment data.
* **Data Integration:** Combining disparate data sources (sales, recalls, sentiment).
* **Looker Studio:** Practical experience with a cloud-based BI tool.
* **Data Cleaning & Preparation:** (Implied, as CSVs are often the result of some preparation).
* **Critical Thinking:** Ability to identify the most relevant business metrics.

## Project Description

The Looker Studio dashboard is fed by four main datasets related to vehicle sales and performance. The visualizations are designed to allow users to explore:
* **Profitability:** Total profit, profit by model, and by dealer.
* **Sales Volume:** Number of units sold, average per sale, and sales by model.
* **Time-based Trends:** Sales and profit performance over time (e.g., by month).
* **Quality & Recalls:** Counts of vehicles recalled by model and affected system, as well as the number of recalls by problem-related keywords.
* **Customer Sentiment (Common Issues):** Analysis of mentions of specific problems (e.g., fluid leaks, warning lights) to identify areas for improvement.

This dashboard offers a holistic business view, enabling stakeholders to monitor performance and make informed decisions.

## Data Sources

The dashboard utilizes the following CSV files, representing sales, recalls, and sentiment data:

* `AU_Daily_Sales.xlsx - AU_Daily_Sales.csv`: Contains daily sales data, including sales ID, date, car ID, dealer ID, temperature, weather conditions, etc.
* `AU_Sales_By_Model.xlsx - Sheet1.csv`: Provides aggregated sales data by model, including year, month, quantity sold, and profit.
* `AU_Car_Recalls.xlsx - Sheet1.csv`: Details vehicle recalls, including date, car ID, affected system, units, and model.
* `AU_Bad_Sentiment.xlsx - page.csv`: Contains sentiment data or negative keywords, with a count of mentions for each problem.

## Key Visualizations & Insights

The dashboard includes charts such as:
* **Scorecards:** For total profit, quantity sold, and average.
* **Bar charts:** Quantity sold and profit by model, profit by dealer ID, record count by model, problem count by keyword.
* **Line charts:** Quantity sold and profit over time (by month).
* **Detailed tables:** Number of recalls by model and affected system.

These visuals quickly allow for:
* Identifying the most profitable models and dealers.
* Observing seasonal trends or peaks in sales.
* Detecting the most recurrent or impactful vehicle issues leading to recalls.
* Understanding the volume and distribution of sales.

## Tools Used

* **Looker Studio (Google Data Studio):** For interactive dashboard design and development.
* **Microsoft Excel / CSV:** As the data storage format and source for Looker Studio.
* **(Optional: If you performed pre-processing with Python)** **Python with Pandas:** For data cleaning and preparation before loading.

## Dashboard Access

You can view an example of the interactive dashboard through the PDF export included in this repository:
* `Sales.pdf`

**(If the dashboard is public in Looker Studio and you have the shared link, you could also add a direct link here for a complete interactive experience)**

## Project Structure