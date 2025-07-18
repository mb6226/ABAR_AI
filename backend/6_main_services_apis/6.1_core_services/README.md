# 6.1 سرویس‌های اصلی (API)

این پوشه شامل سرویس FastAPI برای پیش‌بینی قیمت با مدل LSTM است.

## اجرای سرویس

```bash
cd backend/6_main_services_apis/6.1_core_services
uvicorn main:app --reload
```

## Endpoint اصلی

### POST /predict

پیش‌بینی قیمت بعدی با مدل LSTM بر اساس ۱۰ قیمت آخر.

- **URL:** `/predict`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "prices": [10000, 10010, 10020, 10030, 10040, 10050, 10060, 10070, 10080, 10090]
  }
  ```
  (حداقل ۱۰ مقدار عددی)
- **Response:**
  ```json
  {
    "predicted_price": 10043.91
  }
  ```
- **در صورت خطا:**
  ```json
  { "error": "حداقل 10 مقدار قیمت لازم است." }
  ```

## تست سریع با curl

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"prices": [10000,10010,10020,10030,10040,10050,10060,10070,10080,10090]}'
```

## نکات
- مدل و اسکیلر فقط یکبار بارگذاری می‌شوند.
- ورودی باید حداقل ۱۰ قیمت آخر باشد.
- خروجی، قیمت پیش‌بینی شده بعدی است.
