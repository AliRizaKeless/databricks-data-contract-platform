import csv
import json


def load_contract(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_row(row, constraints):
    errors = []

    temperature = float(row["temperature"])
    wind_speed = float(row["wind_speed"])
    city = row["city"]

    if temperature < constraints["temperature"]["min"] or temperature > constraints["temperature"]["max"]:
        errors.append(f"temperature out of range: {temperature}")

    if wind_speed < constraints["wind_speed"]["min"] or wind_speed > constraints["wind_speed"]["max"]:
        errors.append(f"wind_speed out of range: {wind_speed}")

    if constraints["city"]["not_null"] and city.strip() == "":
        errors.append("city is null or empty")

    return errors


def main():
    contract = load_contract("contracts/weather_contract.json")
    constraints = contract["constraints"]

    total_rows = 0
    failed_rows = 0

    with open("data/weather_sample.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            total_rows += 1
            errors = validate_row(row, constraints)

            if errors:
                failed_rows += 1
                print(f"Row {row_number} FAILED:")
                for error in errors:
                    print(f"  - {error}")

    print("\nValidation Summary")
    print("------------------")
    print(f"Total rows: {total_rows}")
    print(f"Failed rows: {failed_rows}")

    if failed_rows > 0:
        raise SystemExit("Validation failed")

    print("Validation passed")


if __name__ == "__main__":
    main()