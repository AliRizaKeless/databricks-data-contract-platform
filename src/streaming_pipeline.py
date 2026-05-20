from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType


spark = (
    SparkSession.builder
    .appName("StreamingValidationPipeline")
    .getOrCreate()
)

schema = StructType([
    StructField("timestamp", StringType(), True),
    StructField("temperature", StringType(), True),
    StructField("wind_speed", StringType(), True),
    StructField("city", StringType(), True),
])

df = (
    spark.readStream
    .option("header", True)
    .schema(schema)
    .csv("data/streaming_input")
)

validated_df = (
    df
    .withColumn("temperature", col("temperature").cast("double"))
    .withColumn("wind_speed", col("wind_speed").cast("double"))
    .filter(col("city").isNotNull())
    .filter(col("temperature").between(-50, 50))
    .filter(col("wind_speed").between(0, 60))
    .withColumn("processed_at", current_timestamp())
)

query = (
    validated_df.writeStream
    .format("parquet")
    .outputMode("append")
    .option("checkpointLocation", "data/streaming_checkpoint")
    .trigger(availableNow=True)
    .start("data/streaming_output")
)

query.awaitTermination()

print("Streaming batch completed")