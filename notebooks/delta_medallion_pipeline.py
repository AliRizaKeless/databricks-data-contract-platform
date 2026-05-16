# Databricks notebook: Delta Lake Medallion Pipeline
# Bronze -> Silver -> Gold

from pyspark.sql.functions import col, current_timestamp, avg, count

# 1. Read raw CSV data
raw_df = (
    spark.read
    .option("header", True)
    .csv("/FileStore/data/weather_sample_clean.csv")
)

# 2. Bronze layer: raw ingested data
bronze_df = raw_df.withColumn("ingested_at", current_timestamp())

bronze_df.write.format("delta").mode("overwrite").saveAsTable("bronze_weather_data")

# 3. Silver layer: typed and validated data
silver_df = (
    bronze_df
    .withColumn("temperature", col("temperature").cast("double"))
    .withColumn("wind_speed", col("wind_speed").cast("double"))
    .filter(col("city").isNotNull())
    .filter(col("temperature").between(-50, 50))
    .filter(col("wind_speed").between(0, 60))
)

silver_df.write.format("delta").mode("overwrite").saveAsTable("silver_weather_data")

# 4. Gold layer: analytics-ready aggregation
gold_df = (
    silver_df
    .groupBy("city")
    .agg(
        avg("temperature").alias("avg_temperature"),
        avg("wind_speed").alias("avg_wind_speed"),
        count("*").alias("record_count")
    )
)

gold_df.write.format("delta").mode("overwrite").saveAsTable("gold_weather_summary")

display(gold_df)