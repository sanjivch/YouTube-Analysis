# YouTube-Analysis

This data engineering project analyses the YouTube analytics by region.

# Datapipeline workflow - ETL

## Extract
- Currently downloading data from this [kaggle dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new).
- TODO : Replace with a scraping function using YouTube API

## Transform
- Remove `null` and duplicate entries

## Load 
- TODO : Load the processed csv file into a SQLite DB.

# Orchestration
TODO : Use `Prefect` to orchestrate the data pipeline.

# Visualization and Analysis
- TODO : Build a streamlit app/ Apache Superset dashboard that consumes the processed data.
