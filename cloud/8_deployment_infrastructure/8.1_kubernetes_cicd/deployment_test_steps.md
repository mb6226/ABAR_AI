# تست عملیاتی استقرار Kubernetes و CI/CD

این راهنما مراحل تست عملیاتی فایل استقرار Kubernetes و سناریوی CI/CD را برای پروژه ABAR_AI شرح می‌دهد.

---

## ۱. تست فایل استقرار Kubernetes

۱. مطمئن شوید که به کلاستر Kubernetes متصل هستید:
   ```bash
   kubectl config get-contexts
   ```
۲. فایل استقرار را اعمال کنید:
   ```bash
   kubectl apply -f k8s_sample_deployment.yaml
   ```
۳. وضعیت پادها و سرویس را بررسی کنید:
   ```bash
   kubectl get pods
   kubectl get svc
   ```
۴. لاگ پاد را مشاهده کنید:
   ```bash
   kubectl logs <pod-name>
   ```
۵. در صورت نیاز، استقرار را حذف کنید:
   ```bash
   kubectl delete -f k8s_sample_deployment.yaml
   ```

---

## ۲. تست عملیاتی CI/CD (GitHub Actions)

۱. یک commit و push روی main انجام دهید.
۲. وارد GitHub شوید و بخش Actions را بررسی کنید.
۳. مطمئن شوید jobهای build و deploy بدون خطا اجرا شده‌اند.
۴. وضعیت استقرار را در کلاستر بررسی کنید (مانند مرحله قبل).

---

> توجه: برای تست عملیاتی واقعی، باید image و secrets را به صورت واقعی تنظیم کنید.
