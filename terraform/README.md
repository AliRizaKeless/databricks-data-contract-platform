\# Terraform Infrastructure



This folder contains Terraform configuration for provisioning Databricks resources.



\## What it provisions



\- Databricks cluster

\- Databricks notebook deployment



\## Environment



The current environment is:



```text

terraform/environments/dev

Required variables

databricks_host  = "https://your-workspace-url"
databricks_token = "your-token"

Commands

cd terraform/environments/dev
terraform init
terraform plan
terraform apply


Notes

Do not commit real Databricks tokens or secrets to GitHub.
