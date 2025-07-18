# 8.2 تست و مانیتورینگ زیرساخت

در این پوشه، ابزارها و مستندات عملی برای مانیتورینگ و تست زیرساخت Kubernetes قرار دارد.

## فایل‌های مهم
- [`monitoring_stack_overview.md`](monitoring_stack_overview.md): معرفی ابزارهای مانیتورینگ و تست
- [`prometheus_grafana_quickstart.md`](prometheus_grafana_quickstart.md): راه‌اندازی سریع Prometheus و Grafana

## راهنمای سریع تست و مانیتورینگ
1. نصب Helm و اجرای دستورات راه‌اندازی Prometheus و Grafana طبق فایل quickstart
2. مشاهده سرویس‌ها با:
   ```bash
   kubectl get svc
   minikube service grafana
   ```
3. ورود به داشبورد Grafana با نام کاربری و رمز admin

## نکات Troubleshooting
- اگر دسترسی به سرویس‌ها ندارید، وضعیت Minikube و دسترسی docker را بررسی کنید.
- برای تست بار می‌توانید از ابزار k6 استفاده کنید (در فایل overview توضیح داده شده).

## منابع بیشتر
- [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator)
- [Grafana Labs](https://grafana.com/)
- [k6 Load Testing](https://k6.io/)
