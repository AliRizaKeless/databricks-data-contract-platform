from validator import validate_file

if __name__ == "__main__":
    validate_file(
        "data/weather_sample.csv",
        "contracts/weather_contract.json"
    )