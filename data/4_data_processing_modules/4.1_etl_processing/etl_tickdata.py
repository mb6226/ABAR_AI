import csv
import os

input_path = 'data/3_data_collection_storage/3.2_database_datalake/raw/btcusd_binance_1000_tick.csv'
output_path = 'data/4_data_processing_modules/4.1_etl_processing/processed_tickdata.csv'

with open(input_path, newline='') as infile, open(output_path, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['price_usd']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        # نمونه پردازش: افزودن price_usd (همان price)
        row['price_usd'] = row['price']
        writer.writerow(row)

print(f"ETL complete. Processed file saved as {output_path}")
