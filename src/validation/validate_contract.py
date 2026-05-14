import argparse
from validator import validate_file


def main():
    parser = argparse.ArgumentParser(description="Validate data against a contract")

    parser.add_argument("--data", required=True, help="Path to data file (CSV)")
    parser.add_argument("--contract", required=True, help="Path to contract JSON")
    parser.add_argument("--report", default="reports/validation_report.json", help="Path to output report")

    args = parser.parse_args()

    validate_file(
        data_path=args.data,
        contract_path=args.contract,
        report_path=args.report
    )


if __name__ == "__main__":
    main()