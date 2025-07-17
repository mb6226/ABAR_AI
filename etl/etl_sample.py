"""
نمونه اسکریپت ETL برای استخراج، تبدیل و بارگذاری داده‌های بازارهای مالی
"""
import pandas as pd
import sqlalchemy
from pymongo import MongoClient

# استخراج داده نمونه
market_df = pd.DataFrame({
    'symbol': ['AAPL', 'GOOG'],
    'price': [190.5, 2750.0],
    'volume': [100000, 150000],
    'trade_time': pd.to_datetime(['2025-07-17 10:00', '2025-07-17 10:01'])
})

# بارگذاری در دیتابیس SQL
engine = sqlalchemy.create_engine('postgresql://your_user:your_password@localhost:5432/abar_ai')
market_df.to_sql('market_data', engine, if_exists='append', index=False)

# بارگذاری داده نمونه در MongoDB
client = MongoClient('localhost', 27017)
db = client['abar_ai']
db['news_data'].insert_one({'headline': 'Sample news', 'date': '2025-07-17'})
