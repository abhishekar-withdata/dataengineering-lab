# 🚀 Enterprise Lakehouse Sales Platform (Azure | PySpark | ADF)

## 🎯 Business Problem
Enterprise organizations often struggle to unify sales data coming from multiple systems such as SAP, APIs, and flat files. This leads to inconsistent reporting, lack of historical tracking, and poor decision-making.

## 💡 Solution Overview
I designed and implemented a **modern Lakehouse Data Platform** using Azure-aligned architecture to enable:
- Scalable data ingestion
- Reliable transformation pipelines
- Historical tracking using SCD Type 2
- Business-ready analytics layer

---

## 🏗️ Architecture (High-Level)

```
Sources (SAP/CSV/API)
        ↓
Azure Data Factory (Orchestration)
        ↓
Bronze Layer (Raw Data)
        ↓
Databricks (PySpark Processing)
        ↓
Silver Layer (Cleaned Data)
        ↓
Gold Layer (Business Data - SCD2)
        ↓
Azure SQL / Synapse
        ↓
Power BI
```

---

## ⚙️ Tech Stack
- **Azure Data Factory** – Pipeline orchestration
- **PySpark (Databricks aligned)** – Data processing
- **Delta Lake (conceptual)** – ACID & scalable storage
- **Python** – Core development
- **GitHub Actions** – CI/CD
- **Power BI** – Reporting layer

---

## 🔄 Data Pipeline Flow

### 1. Ingestion Layer (Bronze)
- Data ingested from CSV (simulating SAP systems)
- Stored in raw format

### 2. Transformation Layer (Silver)
- Data cleaning (null handling, deduplication)
- Aggregations and joins

### 3. Business Layer (Gold)
- Customer-level aggregations
- SCD Type 2 implementation for historical tracking

---

## 🔥 Key Engineering Features

### ✅ SCD Type 2
Maintains historical changes in customer data using:
- `is_current` flag
- `start_date` and `end_date`

### ✅ Incremental Processing
- Designed for watermark-based loading
- Avoids full refresh and improves performance

### ✅ Data Quality Framework
- Null checks
- Duplicate detection
- Schema validation

### ✅ Logging & Observability
- Centralized logging for pipeline monitoring

### ✅ CI/CD Integration
- Automated test execution using GitHub Actions

---

## 👨‍💼 Manager-Level Contributions

- Designed end-to-end architecture aligned with enterprise standards
n- Structured project into modular layers (ingestion, transformation, quality, orchestration)
- Simulated real team practices (CI/CD, testing, configuration-driven pipelines)
- Focused on scalability, maintainability, and reliability

---

## 📊 Business Impact
- Enabled unified sales reporting
- Improved pipeline efficiency using incremental loads
- Provided historical insights using SCD Type 2

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python pipelines/pipeline_runner.py
```

---

## 🧠 Interview Talking Points

- Designed a scalable lakehouse architecture using Azure components
- Implemented SCD Type 2 for historical data tracking
- Built modular and production-ready ETL pipelines
- Added data quality and logging for reliability
- Integrated CI/CD for engineering best practices

---

## 📌 Future Enhancements
- Real-time streaming (Kafka / Event Hub)
- Data lineage and governance
- Terraform for infrastructure as code

---

## 📎 Architecture Diagram

Refer to: `architecture/architecture.html`
