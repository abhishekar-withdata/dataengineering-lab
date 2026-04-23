# Enterprise Data Platform (90 LPA Project)

## Overview
This project simulates a real-world enterprise data engineering system using Azure-like architecture, PySpark, and ETL pipelines.

## Problem Statement
Build a scalable data platform to process sales data from SAP-like systems and enable analytics.

## Architecture
- Ingestion: CSV/API (ADF simulated)
- Processing: PySpark
- Storage: Bronze/Silver/Gold
- Serving: SQL/Power BI

## Key Features
- Incremental loading
- SCD Type 2
- Data quality checks
- Logging

## How to Run
pip install -r requirements.txt
python pipeline.py

## Interview Talking Points
- Designed lakehouse architecture
- Implemented SCD2
- Built scalable pipelines
