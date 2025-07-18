# مرحله ۵: ساخت و آموزش مدل LSTM برای پیش‌بینی سری زمانی تیک دیتا

## ساختار پوشه
- 5.1_model_selection: انتخاب مدل مناسب (LSTM)
  - model_selection.md
- 5.2_training_evaluation: آموزش و ارزیابی مدل
  - lstm_train.py
- 5.3_testing_validation: تست و اعتبارسنجی مدل
  - lstm_test.py
- 5.4_documentation: مستندسازی مدل و نتایج
  - modeling_report.md

---

## روند اجرایی عملی مرحله ۵

۱. **انتخاب مدل مناسب**
   - فایل: `5.1_model_selection/model_selection.md`
   - توضیح: مدل LSTM به عنوان مدل پایه برای داده‌های تیک انتخاب شد.

۲. **آموزش و ارزیابی مدل**
   - فایل: `5.2_training_evaluation/lstm_train.py`
   - ورودی: `../../data/4_data_processing_modules/4.1_etl_processing/processed_tickdata.csv`
   - خروجی: `lstm_model.h5`
   - نتیجه: مدل LSTM با داده‌های قیمت آموزش داده می‌شود و مدل ذخیره می‌گردد.

۳. **تست و اعتبارسنجی مدل**
   - فایل: `5.3_testing_validation/lstm_test.py`
   - ورودی: `lstm_model.h5` و داده پردازش‌شده
   - خروجی: `lstm_predictions.csv`
   - نتیجه: پیش‌بینی قیمت‌ها توسط مدل انجام و خروجی ذخیره می‌شود.

۴. **مستندسازی مدل و نتایج**
   - فایل: `5.4_documentation/modeling_report.md`
   - توضیح: مستندسازی مراحل، نتایج آموزش و تست مدل، پیشنهادات بهبود و مقایسه با سایر مدل‌ها

---

## خلاصه خروجی‌ها
- مدل آموزش‌دیده: `lstm_model.h5`
- پیش‌بینی مدل: `lstm_predictions.csv`
- گزارش مدل‌سازی: `modeling_report.md`

تمام مراحل به صورت ماژولار و قابل اجرا در پوشه ۵_LSTM پیاده‌سازی شده است.
