# Databricks notebook: MLflow Weather Model

import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from pyspark.sql.functions import col

# Gold table oku
df = spark.table("silver_weather_data")

# Pandas'a çevir (küçük veri için)
pdf = df.select("temperature", "wind_speed").toPandas()

# Feature / target
X = pdf[["wind_speed"]]
y = pdf["temperature"]

# MLflow başlat
mlflow.set_experiment("/Shared/weather_prediction")

with mlflow.start_run():

    model = LinearRegression()
    model.fit(X, y)

    # Tahmin
    predictions = model.predict(X)

    # Basit metric
    mse = ((predictions - y) ** 2).mean()

    # Log
    mlflow.log_param("model", "LinearRegression")
    mlflow.log_metric("mse", mse)

    mlflow.sklearn.log_model(model, "model")

    print(f"Model trained. MSE: {mse}")