import shutil
import os

src = '../3.1_data_collection/btcusd_binance_1000_tick.csv'
dst = 'raw/btcusd_binance_1000_tick.csv'

os.makedirs('raw', exist_ok=True)

if os.path.exists(src):
    shutil.copy2(src, dst)
    print(f'فایل {src} به {dst} منتقل شد.')
else:
    print(f'فایل {src} پیدا نشد.')
