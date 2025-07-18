import json
import random
import time
from datetime import datetime, timedelta

# تنظیمات اولیه
start_price = 60000
start_time = datetime.utcfromtimestamp(1721251200)
num_records = 1000
interval_sec = 60  # هر کندل یک دقیقه

records = []
last_close = start_price
for i in range(num_records):
    ts = int((start_time + timedelta(seconds=i * interval_sec)).timestamp())
    open_ = last_close
    high = open_ + random.uniform(0, 100)
    low = open_ - random.uniform(0, 100)
    close = random.uniform(low, high)
    volume = round(random.uniform(0.5, 2.0), 2)
    records.append({
        "timestamp": ts,
        "open": round(open_, 2),
        "high": round(high, 2),
        "low": round(low, 2),
        "close": round(close, 2),
        "volume": volume
    })
    last_close = close

with open("btcusd_binance_sample_1000.json", "w") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print(f"1000 رکورد نمونه BTCUSD تولید و ذخیره شد.")
