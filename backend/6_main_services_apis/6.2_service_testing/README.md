# 6.2 تست و اعتبارسنجی سرویس‌ها

در این پوشه اسکریپت‌های تست سرویس‌های Backend قرار می‌گیرد.

## تست عملی API

- فایل `test_api.py` یک تست ساده برای endpoint پیش‌بینی (`/predict`) است.
- برای اجرا:

```bash
python test_api.py
```

- خروجی شامل status code و پاسخ API خواهد بود.

## وابستگی‌ها
- نیاز به اجرای سرویس FastAPI (در پوشه ۶.۱) و نصب پکیج `requests` دارد:

```bash
pip install requests
```
