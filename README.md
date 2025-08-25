🏅 Sports Analytics Pipeline for Singapore Athletics Association (SAA)

Overview

This project is a comprehensive sports analytics platform designed to extract, clean, transform, and analyze athletic performance data spanning 15 years. The pipeline consolidates structured and unstructured data from multiple sources into BigQuery, enabling powerful insights through interactive dashboards and reports.

✨ Key Features

- Data Extraction: Automated ingestion from diverse formats:

- MS Access, CSV, Excel, Word, PDF

- Legacy migration from phpMyAdmin MySQL into BigQuery

Data Pipeline:

- Custom ETL pipeline built on Cloud Run functions

- Google Pub/Sub and Cloud Storage used to orchestrate and trigger workflows

- Continuous cleaning, transformation, and loading into BigQuery

- Handles a large proportion of unstructured data

Analytics & Reporting:

- Frontend interfaces via Streamlit for functional reporting and database query

- Dashboards in Looker Studio for interactive data visualization

- Automated reports for coaches and managers to identify promising and top athletes for prioritization and funding

Coverage:

- Over 15 years of historical performance data

- Both local and international competitions

🛠️ Tech Stack

- Data Sources: MS Access, CSV, Excel, Word, PDF, MySQL (phpMyAdmin)

- ETL & Orchestration: Python, Pandas, Cloud Run, Pub/Sub, Cloud Storage

- Data Warehouse: Google BigQuery

- Visualization: Streamlit, Looker Studio

🚀 Outcomes

- Unified analytics platform for athletic performance data

- Automated, cloud-native ETL pipeline ensuring data freshness

- Actionable insights for athlete development and funding decisions

📊 Example Use Cases

- Monitor athlete progress across seasons and competitions

- Compare performances across event categories and regions

- Identify emerging talent for strategic funding and training support
