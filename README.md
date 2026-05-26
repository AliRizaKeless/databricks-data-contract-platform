# Data Contract-Driven Lakehouse Platform on Databricks

## Recruiter Summary

This project demonstrates a production-oriented Databricks Lakehouse platform with contract-driven data validation, PySpark-based processing, Delta Lake medallion architecture, Unity Catalog governance, MLflow model tracking, CI/CD automation, and Infrastructure as Code using Terraform.

It reflects real-world data engineering practices used in modern cloud-based analytics environments.

---

## Use Case

In modern data platforms, data quality issues can silently break analytics, dashboards, and machine learning workflows.

This project demonstrates how a contract-driven validation layer can prevent bad data from entering the lakehouse, ensuring reliable downstream analytics and ML workflows.

It simulates a real-world scenario where data engineers must guarantee data quality before ingestion into a Databricks-based platform.

---

## End-to-End Flow

1. Raw data is ingested (batch or streaming)
2. Data is validated using data contracts
3. Invalid data is rejected and logged
4. Valid data is written to Delta Lake (Bronze → Silver → Gold)
5. Data is used for analytics and ML (MLflow)
6. Infrastructure is provisioned via Terraform

---

## Architecture

Data Source (CSV / Streaming)
↓
Validation Layer (Data Contracts)
↓
Bronze (Raw Delta)
↓
Silver (Cleaned Data)
↓
Gold (Analytics)
↓
MLflow (Model Training)


---

## Tech Stack

- Python
- PySpark
- Databricks
- Delta Lake
- Unity Catalog
- MLflow
- GitHub Actions (CI/CD)
- Terraform (Infrastructure as Code)

---

## Features

- Contract-driven data validation
- Data quality enforcement (schema + constraints)
- Validation reporting (JSON)
- Logging
- CLI-based execution
- Batch and streaming pipelines
- Delta Lake medallion architecture
- ML model training with MLflow
- Databricks notebook integration
- CI/CD pipeline with GitHub Actions
- Infrastructure provisioning with Terraform

---

## Delta Lake Medallion Pipeline

- Bronze: Raw ingested data
- Silver: Cleaned and validated data
- Gold: Aggregated analytics-ready data

---

## MLflow Model Tracking

- Linear Regression model for temperature prediction
- Trained on Silver layer data
- Logs parameters, metrics (MSE), and model artifacts

---

## Unity Catalog Governance

- Catalog and schema organization
- Managed Delta tables
- Governance-ready structure for access control and discoverability

---

## Streaming Pipeline

- Built with Spark Structured Streaming
- Processes incoming files in near real-time
- Applies validation rules before writing output
- Uses checkpointing for fault tolerance

---

## Terraform Infrastructure

This project includes Infrastructure as Code for Databricks:

- Databricks cluster provisioning
- Notebook deployment
- Environment-based configuration

---

## Quick Demo

### Run validation (failing example)

```bash
py src/validation/validate_contract.py --data data/weather_sample.csv --contract contracts/weather_contract.json

Run validation (successful example)
py src/validation/validate_contract.py --data data/weather_sample_clean.csv --contract contracts/weather_contract.json --report reports/validation_report_clean.json

Run pipeline
py src/pipeline.py

Project Structure
contracts/
data/
notebooks/
reports/
src/
tests/
terraform/
.github/workflows/

Skills Demonstrated
- Modern data platform design
- Databricks lakehouse architecture
- Distributed data processing with PySpark
- Data contracts and data quality engineering
- CI/CD and automation
- Infrastructure as Code (Terraform)
- Streaming data processing
- ML integration with MLflow

Status

Production-style portfolio project demonstrating real-world data engineering practices.

