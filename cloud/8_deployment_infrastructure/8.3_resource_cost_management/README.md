# Resource & Cost Management (مدیریت منابع و هزینه‌ها)

این بخش راهنمای عملی برای مدیریت منابع و هزینه‌ها در زیرساخت ابری پروژه را ارائه می‌دهد.

## 1. مقدمه
مدیریت منابع و هزینه‌ها در محیط‌های ابری (مانند Kubernetes) برای جلوگیری از هدررفت منابع و کنترل هزینه‌ها حیاتی است. ابزارهای متن‌باز مانند [Kubecost](https://kubecost.com/) و داشبوردهای ابری (AWS, GCP, Azure) می‌توانند کمک‌کننده باشند.

---

## 2. نصب و راه‌اندازی Kubecost روی Minikube

Kubecost ابزاری متن‌باز برای پایش و مدیریت هزینه‌ها و منابع در کلاستر Kubernetes است.

### مراحل نصب سریع:

1. **نصب Helm (در صورت نیاز):**
   ```bash
   curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
   ```

2. **اضافه کردن ریپازیتوری Kubecost:**
   ```bash
   helm repo add kubecost https://kubecost.github.io/cost-analyzer/
   helm repo update
   ```

3. **نصب Kubecost روی Minikube:**
   ```bash
   helm install kubecost kubecost/cost-analyzer \
     --namespace kubecost --create-namespace \
     --set kubecostToken="demo-token"
   ```

4. **دسترسی به داشبورد Kubecost:**
   ```bash
   kubectl port-forward --namespace kubecost deployment/kubecost-cost-analyzer 9090
   ```
   سپس در مرورگر باز کنید: [http://localhost:9090](http://localhost:9090)

### منابع بیشتر:
- [Kubecost Quickstart](https://docs.kubecost.com/install)
- [Kubecost on Minikube](https://docs.kubecost.com/install/minikube)

---

## 3. مدیریت هزینه در سرویس‌دهنده‌های ابری (Cloud Billing)

اگر پروژه روی سرویس‌دهنده‌های ابری (AWS, GCP, Azure) اجرا می‌شود:

- **AWS Cost Explorer:** [راهنما](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- **GCP Billing Dashboard:** [راهنما](https://cloud.google.com/billing/docs/how-to/manage-billing-account)
- **Azure Cost Management:** [راهنما](https://learn.microsoft.com/en-us/azure/cost-management-billing/)

### نکات عملی:
- برای هر سرویس/کلاستر، بودجه و آستانه هشدار تعریف کنید.
- از تگ‌گذاری منابع برای ردیابی هزینه‌ها استفاده کنید.
- گزارش‌های دوره‌ای هزینه را بررسی و تحلیل کنید.

---

## 4. نکات و ابزارهای تکمیلی

- [Kube-resource-report](https://github.com/hjacobs/kube-resource-report): گزارش منابع مصرفی کلاستر
- [Goldilocks](https://github.com/FairwindsOps/goldilocks): پیشنهاد بهینه‌سازی resource requests/limits
- [Prometheus + Grafana](../8.2_monitoring_testing/): برای پایش منابع و هشداردهی

---

## 5. عیب‌یابی و سوالات متداول

- اگر Kubecost اجرا نشد، با دستور `kubectl get pods -n kubecost` وضعیت را بررسی کنید.
- برای حذف Kubecost:
  ```bash
  helm uninstall kubecost -n kubecost
  kubectl delete namespace kubecost
  ```

---

**این راهنما را با توجه به نیازهای پروژه خود تکمیل و شخصی‌سازی کنید.**
