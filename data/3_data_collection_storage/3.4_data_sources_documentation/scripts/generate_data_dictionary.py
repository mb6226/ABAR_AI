import json

# نمونه ساده برای تولید data dictionary از روی ساختار داده
fields = [
    {"name": "timestamp", "type": "int", "description": "زمان ثبت تیک (epoch ms)"},
    {"name": "price", "type": "float", "description": "قیمت معامله"},
    {"name": "quantity", "type": "float", "description": "حجم معامله"},
    {"name": "trade_id", "type": "int", "description": "شناسه یکتا برای هر معامله"},
    {"name": "is_buyer_maker", "type": "bool", "description": "آیا خریدار سفارش‌دهنده است؟"}
]

with open('data/3_data_collection_storage/3.4_data_sources_documentation/metadata/data_dictionary.json', 'w') as f:
    json.dump(fields, f, ensure_ascii=False, indent=2)

print("data_dictionary.json generated.")
