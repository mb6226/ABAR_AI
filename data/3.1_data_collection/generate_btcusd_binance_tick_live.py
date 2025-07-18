import json
import websocket
import threading
import time

# تنظیمات
symbol = "btcusdt"
stream_url = f"wss://stream.binance.com:9443/ws/{symbol}@trade"
output_file = "btcusd_binance_sample_1000_tick.json"
max_records = 1000
records = []

# تابع دریافت داده از وب‌سوکت
def on_message(ws, message):
    global records
    data = json.loads(message)
    record = {
        "timestamp": int(data['T'] // 1000),
        "price": float(data['p']),
        "quantity": float(data['q']),
        "trade_id": data['t'],
        "is_buyer_maker": data['m']
    }
    records.append(record)
    print(f"دریافت تیک {len(records)}: {record}")
    if len(records) >= max_records:
        ws.close()
        with open(output_file, "w") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        print(f"{max_records} تیک ذخیره شد و اسکریپت متوقف شد.")

def on_error(ws, error):
    print(f"خطا: {error}")

def on_close(ws, close_status_code, close_msg):
    print("اتصال بسته شد.")

def on_open(ws):
    print("اتصال به وب‌سوکت برقرار شد.")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(stream_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    ws.run_forever()
