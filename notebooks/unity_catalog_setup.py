# Databricks notebook: Unity Catalog setup example

# Catalog and schema setup
spark.sql("CREATE CATALOG IF NOT EXISTS data_contract_platform")
spark.sql("CREATE SCHEMA IF NOT EXISTS data_contract_platform.weather")

# Managed Delta tables in Unity Catalog
spark.sql("""
CREATE TABLE IF NOT EXISTS data_contract_platform.weather.bronze_weather_data
USING DELTA
AS SELECT * FROM bronze_weather_data
""")

spark.sql("""
CREATE TABLE IF NOT EXISTS data_contract_platform.weather.silver_weather_data
USING DELTA
AS SELECT * FROM silver_weather_data
""")

spark.sql("""
CREATE TABLE IF NOT EXISTS data_contract_platform.weather.gold_weather_summary
USING DELTA
AS SELECT * FROM gold_weather_summary
""")