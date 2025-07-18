# مستندسازی فرآیند ETL

در این فایل، مراحل و منطق پردازش اولیه داده‌های تیک (ETL) پروژه ABAR_AI شرح داده شده است.

1. خواندن داده خام از دیتالیک (CSV)
2. افزودن فیلد جدید price_usd به هر ردیف
3. ذخیره داده پردازش‌شده در فایل جدید

> اسکریپت etl_tickdata.py این مراحل را به صورت خودکار انجام می‌دهد.

## مستندسازی فرآیند آماده‌سازی داده

۱. انتقال فایل CSV به دیتالیک (raw)
۲. واردسازی به دیتابیس SQLite
۳. اعتبارسنجی داده و تولید گزارش
۴. تولید دیکشنری داده
۵. پردازش اولیه (ETL)
۶. تست صحت داده پردازش‌شده
۷. ذخیره گزارش تست و مستندسازی نهایی

گزارش تست: در فایل test_report_sample.md و test_report.txt موجود است.
گزارش اعتبارسنجی: در data/3_data_collection_storage/3.3_data_validation_backup/raw_validation/validation_report.txt
دیکشنری داده: در data/3_data_collection_storage/3.4_data_sources_documentation/metadata/data_dictionary.json

تمام مراحل طبق روند اجرایی انجام شد و داده processed_tickdata.csv آماده مرحله بعد است.
