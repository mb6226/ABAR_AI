import csv
import os

input_path = 'data/4_data_processing_modules/4.1_etl_processing/processed_tickdata.csv'

if not os.path.exists(input_path):
    print("Processed file not found. Run ETL first.")
    exit(1)

with open(input_path, newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    assert all('price_usd' in row for row in rows), "Missing price_usd field in processed data."
    print(f"Test passed: All {len(rows)} rows have price_usd field.")

with open('data/4_data_processing_modules/4.2_module_testing/test_report.txt', 'w') as report:
    report.write(f"Test passed: All {len(rows)} rows have price_usd field.\n")
