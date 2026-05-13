import json
import csv


def load_contract(contract_path):
    with open(contract_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_row(row, contract):
    errors = []
    constraints = contract.get("constraints", {})

    for field, rules in constraints.items():
        value = row.get(field)

        # not null kontrolü
        if isinstance(rules, dict) and rules.get("not_null"):
            if value is None or value.strip() == "":
                errors.append(f"{field} is null or empty")
                continue

        # numeric kontrol
        try:
            numeric_value = float(value)
        except (TypeError, ValueError):
            continue

        if "min" in rules and numeric_value < rules["min"]:
            errors.append(f"{field} below min: {numeric_value}")

        if "max" in rules and numeric_value > rules["max"]:
            errors.append(f"{field} above max: {numeric_value}")

    return errors


def validate_file(data_path, contract_path):
    contract = load_contract(contract_path)

    total = 0
    failed = 0

    with open(data_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader, start=2):
            total += 1
            errors = validate_row(row, contract)

            if errors:
                failed += 1
                print(f"Row {i} FAILED:")
                for e in errors:
                    print(f"  - {e}")

    print("\nSummary")
    print("--------")
    print(f"Total: {total}")
    print(f"Failed: {failed}")

    if failed > 0:
        raise SystemExit("Validation failed")

    print("Validation passed")