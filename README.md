\# Databricks Data Contract Platform



A contract-driven data validation platform designed for modern lakehouse architectures.

## Recruiter Summary

This project demonstrates a production-oriented Databricks Lakehouse workflow with contract-driven data validation, PySpark processing, Delta Lake medallion architecture, Unity Catalog governance, MLflow model tracking, CI/CD automation, logging, and validation reporting.

It is designed to reflect real-world data platform engineering practices used in modern cloud-based analytics environments.

\## Project Goal



This project demonstrates how to validate incoming data against predefined data contracts before loading it into a lakehouse environment.



It focuses on:



\- Data contracts

\- Schema and quality validation

\- PySpark-based validation

\- Validation reports

\- Logging

\- CI/CD with GitHub Actions

\- Databricks-ready notebook structure



\## Why This Project Matters



In real-world data platforms, data quality issues can break downstream analytics, dashboards, and machine learning workflows.



This project solves that by validating data before it is trusted by downstream systems.



\## Tech Stack



\- Python

\- PySpark

\- Databricks

\- Delta Lake-ready architecture

\- GitHub Actions

\- JSON data contracts

## Skills Demonstrated

This project demonstrates practical experience with:

- Modern data platform design
- Databricks-ready data validation workflows
- PySpark-based distributed data processing
- Data contracts and data quality rules
- Fail-fast pipeline design
- CI/CD with GitHub Actions
- Logging and validation reporting
- Lakehouse-oriented project structure

## How It Works

1. A data contract defines the expected structure and quality rules for a dataset.
2. Incoming data is validated against the contract.
3. Invalid rows are detected and reported.
4. A validation report is generated as JSON.
5. The pipeline fails if data quality rules are violated.
6. GitHub Actions runs the validation automatically on every push.

## Architecture

The platform follows a contract-driven data validation approach:

Data Source (CSV / API)
        ↓
Ingestion Layer
        ↓
Validation Engine (Contract-based)
        ↓
Validated / Rejected Data
        ↓
Delta Lake (Databricks-ready)
        ↓
Analytics / Downstream Systems

The validation layer ensures that only high-quality, contract-compliant data is allowed into the lakehouse.

## Delta Lake Medallion Pipeline

The project includes a Databricks-ready Delta Lake pipeline following the medallion architecture:

- Bronze: raw ingested weather data
- Silver: cleaned and validated weather data
- Gold: analytics-ready weather summary by city

This demonstrates how validated data can move through a lakehouse pipeline using Delta tables.

## MLflow Model Tracking

The project includes a simple machine learning workflow using MLflow:

- A Linear Regression model predicts temperature based on wind speed
- Training is performed on the Silver layer data
- MLflow is used to track:
  - Parameters
  - Metrics (MSE)
  - Trained model artifacts

This demonstrates how a data platform can support downstream machine learning workflows.

## Unity Catalog Governance

The project includes a Databricks Unity Catalog setup example:

- Catalog creation
- Schema creation
- Managed Delta tables
- Governance-ready table organization

This demonstrates how the lakehouse tables can be structured for centralized governance, access control, and discoverability in Databricks.

\## Current Features



\- Contract-based validation

\- Failed row detection

\- Validation report generation

\- Logging

\- CLI support

\- PySpark validation

\- GitHub Actions pipeline

\- Databricks notebook example



\## Example Validation Command



```bash

py src/validation/validate\_contract.py --data data/weather\_sample.csv --contract contracts/weather\_contract.json

Project Structure

contracts/
data/
notebooks/
reports/
src/
tests/
.github/workflows/

Status

Work in progress.

## Quick Demo

### Run validation (failing example)

```bash
py src/validation/validate_contract.py --data data/weather_sample.csv --contract contracts/weather_contract.json