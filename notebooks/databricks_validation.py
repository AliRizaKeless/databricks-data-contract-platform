# Databricks notebook version

from pyspark.sql.functions import col

# Data yükle
df = spark.read.option("header", True).csv("/FileStore/data/weather_sample.csv")

# Validation logic
failed_df = df.filter(
    (col("temperature").cast("double") > 50) |
    (col("temperature").cast("double") < -50) |
    (col("wind_speed").cast("double") > 60) |
    (col("wind_speed").cast("double") < 0) |
    (col("city").isNull()) |
    (col("city") == "")
)

# Sonuçlar
total_rows = df.count()
failed_rows = failed_df.count()

print(f"Total rows: {total_rows}")
print(f"Failed rows: {failed_rows}")

display(failed_df)