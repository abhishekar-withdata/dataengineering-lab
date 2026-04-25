# High-Level Architecture (Text Diagram)

Sources (API, CSV, Streaming)
        ↓
Ingestion (ADF / Fabric Pipelines)
        ↓
Bronze Layer (Raw Delta)
        ↓
Silver Layer (Cleaned)
        ↓
Gold Layer (Business + Features)
        ↓
ML Models + Power BI Dashboards
        ↓
Governance & Security Layer

## Notes
- Supports batch + streaming
- Scalable Lakehouse design
- Optimized for cost and performance