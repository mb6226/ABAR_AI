# 8.1 راه‌اندازی Kubernetes و CI/CD

در این پوشه، اسکریپت‌ها و مستندات عملی برای راه‌اندازی کلاستر Kubernetes و پیاده‌سازی CI/CD پروژه قرار دارد.

## فایل‌های مهم
- [`k8s_sample_deployment.yaml`](k8s_sample_deployment.yaml): نمونه فایل استقرار (Deployment و Service)
- [`deployment_test_steps.md`](deployment_test_steps.md): راهنمای تست عملیاتی و گام‌به‌گام
- [`ci_cd_pipeline_sample.md`](ci_cd_pipeline_sample.md): نمونه سناریوی CI/CD با GitHub Actions

## راهنمای سریع اجرا
1. نصب و راه‌اندازی Minikube و kubectl (برای تست رایگان و لوکال)
2. اجرای دستورات زیر:
   ```bash
   minikube start
   kubectl apply -f k8s_sample_deployment.yaml
   kubectl get pods
   kubectl get svc
   ```
3. مشاهده لاگ پاد:
   ```bash
   kubectl logs <pod-name>
   ```
4. حذف استقرار:
   ```bash
   kubectl delete -f k8s_sample_deployment.yaml
   ```

## نکات Troubleshooting
- اگر پادها در وضعیت InvalidImageName بودند، مقدار image را به یک ایمیج معتبر (مثلاً nginx:latest) تغییر دهید.
- اگر سرویس LoadBalancer در Minikube external-ip ندارد، از دستور زیر برای مشاهده سرویس در مرورگر استفاده کنید:
  ```bash
  minikube service abarai-fastapi-service
  ```

## منابع بیشتر
- [مستندات رسمی Kubernetes](https://kubernetes.io/docs/)
- [Minikube Getting Started](https://minikube.sigs.k8s.io/docs/start/)
