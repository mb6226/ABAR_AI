import sqlite3
import csv
import os

# مسیر فایل CSV و دیتابیس
import pathlib

# مسیر مطلق فایل CSV و دیتابیس
base_dir = pathlib.Path(__file__).parent.resolve()
csv_path = str(base_dir / "raw/btcusd_binance_1000_tick.csv")
db_path = str(base_dir / "abarai_tickdata.db")

table_name = "btcusd_binance_tick"

# ساخت جدول اگر وجود ندارد
def create_table(conn):
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            timestamp INTEGER,
            price REAL,
            quantity REAL,
            trade_id INTEGER,
            is_buyer_maker BOOLEAN
        )
    """)
    conn.commit()

# وارد کردن داده‌ها از CSV به دیتابیس
def import_csv_to_db():
    conn = sqlite3.connect(db_path)
    create_table(conn)
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [
            (
                int(row['timestamp']),
                float(row['price']),
                float(row['quantity']),
                int(row['trade_id']),
                bool(row['is_buyer_maker'])
            ) for row in reader
        ]
    conn.executemany(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)", rows)
    conn.commit()
    conn.close()
    print(f"واردسازی داده‌ها از {csv_path} به {db_path} انجام شد.")

if __name__ == "__main__":
    import_csv_to_db()
