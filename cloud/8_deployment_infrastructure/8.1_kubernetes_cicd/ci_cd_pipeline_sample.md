# نمونه سناریوی CI/CD برای پروژه ABAR_AI

این فایل یک سناریوی ساده CI/CD را برای استقرار خودکار backend (FastAPI) و frontend (Streamlit) ارائه می‌دهد.

## مراحل پیشنهادی:

1. **ساخت ایمیج Docker** برای backend و frontend
2. **Push** ایمیج‌ها به DockerHub یا Registry خصوصی
3. **استفاده از GitHub Actions یا GitLab CI** برای اجرای خودکار مراحل build و deploy
4. **استقرار روی کلاستر Kubernetes** با استفاده از فایل‌های yaml

## نمونه job در GitHub Actions

```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [ main ]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build Docker image
        run: docker build -t <your-dockerhub-username>/abarai-fastapi:latest ./backend/6_main_services_apis/6.1_core_services
      - name: Login to DockerHub
        run: echo ${{ secrets.DOCKERHUB_TOKEN }} | docker login -u ${{ secrets.DOCKERHUB_USERNAME }} --password-stdin
      - name: Push Docker image
        run: docker push <your-dockerhub-username>/abarai-fastapi:latest
      - name: Deploy to Kubernetes
        run: kubectl apply -f cloud/8_deployment_infrastructure/8.1_kubernetes_cicd/k8s_sample_deployment.yaml
```

> توجه: مقادیر `<your-dockerhub-username>` و secrets را با اطلاعات واقعی جایگزین کنید.
