# راه‌اندازی سریع Prometheus و Grafana روی Minikube

## نصب Prometheus و Grafana با Helm

۱. نصب Helm (در صورت نیاز):
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

۲. افزودن ریپازیتوری chart:
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

۳. نصب Prometheus:
```bash
helm install prometheus prometheus-community/prometheus
```

۴. نصب Grafana:
```bash
helm install grafana grafana/grafana --set adminPassword=admin
```

۵. مشاهده سرویس‌ها:
```bash
kubectl get svc
```

۶. دسترسی به داشبورد Grafana (در Minikube):
```bash
minikube service grafana
```

۷. ورود به داشبورد با نام کاربری `admin` و رمز `admin`

---

> برای تست بار و عملکرد می‌توانید از ابزار k6 استفاده کنید.
