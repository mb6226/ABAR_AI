import csv
import sys

csv_path = sys.argv[1] if len(sys.argv) > 1 else '../../3.2_database_datalake/raw/btcusd_binance_1000_tick.csv'
report_path = '../raw_validation/validation_report.txt'

required_fields = ["timestamp", "price", "quantity", "trade_id", "is_buyer_maker"]
errors = []
row_count = 0

with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader, 1):
        row_count += 1
        for field in required_fields:
            if field not in row or row[field] == '':
                errors.append(f"Row {i}: Missing or empty field '{field}'")
        try:
            int(row['timestamp'])
            float(row['price'])
            float(row['quantity'])
            int(row['trade_id'])
            assert row['is_buyer_maker'] in ['True', 'False', 'true', 'false', '0', '1']
        except Exception as e:
            errors.append(f"Row {i}: Invalid data type - {e}")

with open(report_path, 'w') as f:
    f.write(f"Total rows checked: {row_count}\n")
    if errors:
        f.write(f"Errors found: {len(errors)}\n")
        for err in errors:
            f.write(err + '\n')
    else:
        f.write("No errors found. Data is valid.\n")

print(f"Validation complete. Report saved to {report_path}")
