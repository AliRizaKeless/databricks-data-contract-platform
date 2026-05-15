import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def load_contract(contract_path):
    with open(contract_path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_spark_session():
    return (
        SparkSession.builder
        .appName("DataContractValidation")
        .getOrCreate()
    )


def validate_with_spark(data_path, contract_path):
    spark = create_spark_session()
    contract = load_contract(contract_path)
    constraints = contract.get("constraints", {})

    df = spark.read.option("header", True).csv(data_path)

    failed_conditions = []

    for field, rules in constraints.items():
        if rules.get("not_null"):
            failed_conditions.append(col(field).isNull() | (col(field) == ""))

        if "min" in rules:
            failed_conditions.append(col(field).cast("double") < rules["min"])

        if "max" in rules:
            failed_conditions.append(col(field).cast("double") > rules["max"])

    failed_df = df.filter(failed_conditions[0])

    for condition in failed_conditions[1:]:
        failed_df = failed_df.union(df.filter(condition))

    total_rows = df.count()
    failed_rows = failed_df.dropDuplicates().count()

    print("Spark Validation Summary")
    print("------------------------")
    print(f"Total rows: {total_rows}")
    print(f"Failed rows: {failed_rows}")

    if failed_rows > 0:
        failed_df.show(truncate=False)
        raise SystemExit("Spark validation failed")

    print("Spark validation passed")


if __name__ == "__main__":
    validate_with_spark(
        "data/weather_sample.csv",
        "contracts/weather_contract.json"
    )