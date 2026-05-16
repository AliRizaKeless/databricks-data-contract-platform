\# Databricks Data Contract Platform



A contract-driven data validation platform designed for modern lakehouse architectures.



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

## How It Works

1. A data contract defines the expected structure and quality rules for a dataset.
2. Incoming data is validated against the contract.
3. Invalid rows are detected and reported.
4. A validation report is generated as JSON.
5. The pipeline fails if data quality rules are violated.
6. GitHub Actions runs the validation automatically on every push.

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