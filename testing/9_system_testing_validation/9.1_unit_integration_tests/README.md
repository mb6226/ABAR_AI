# 9.1 تست واحد و یکپارچه‌سازی (Unit & Integration Testing)

در این پوشه، اسکریپت‌ها و مستندات مربوط به تست واحد (unit test) و تست یکپارچه‌سازی (integration test) قرار می‌گیرد.

## نمونه عملی تست واحد (pytest)

1. نصب pytest (در محیط مجازی):
   ```bash
   pip install pytest
   ```

2. نمونه تست ساده:
   فایل `test_sample.py`:
   ```python
   def add(a, b):
       return a + b

   def test_add():
       assert add(2, 3) == 5
   ```

3. اجرای تست:
   ```bash
   pytest test_sample.py
   ```

## نکته
- تست‌های یکپارچه‌سازی را نیز می‌توانید مشابه تست‌های واحد، با ارتباط بین ماژول‌ها بنویسید.
- گزارش تست‌ها را در همین پوشه قرار دهید.
