import subprocess
import sys


def run_validation():
    command = [
        "py",
        "src/validation/validate_contract.py",
        "--data", "data/weather_sample.csv",
        "--contract", "contracts/weather_contract.json"
    ]

    result = subprocess.run(command)

    if result.returncode != 0:
        print("Pipeline FAILED")
        sys.exit(1)

    print("Pipeline SUCCESS")


if __name__ == "__main__":
    run_validation()