-- ساختار جداول دیتابیس SQL برای ذخیره‌سازی داده‌های بازارهای مالی
CREATE TABLE IF NOT EXISTS market_data (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    price FLOAT,
    volume BIGINT,
    trade_time TIMESTAMP
);

CREATE TABLE IF NOT EXISTS fundamental_data (
    id SERIAL PRIMARY KEY,
    company VARCHAR(100),
    report_date DATE,
    revenue FLOAT,
    profit FLOAT
);
