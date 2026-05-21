terraform {
  required_version = ">= 1.6.0"

  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "~> 1.50"
    }
  }
}

provider "databricks" {
  host  = var.databricks_host
  token = var.databricks_token
}

# Create a cluster

resource "databricks_cluster" "this" {
  cluster_name            = "data-contract-cluster"
  spark_version           = "13.3.x-scala2.12"
  node_type_id            = "Standard_DS3_v2"
  autotermination_minutes = 60

  num_workers = 1
}

# Create a notebook

resource "databricks_notebook" "validation_notebook" {
  path     = "/Shared/data_contract_validation"
  language = "PYTHON"
  source   = "${path.module}/../../../notebooks/databricks_validation.py"
}