# flask-kuber
Сайт на http://note.mikop.su
# 1. Клонируем репозиторий
```bash
git clone http://github.com/app
cd app
```
# 2. Собираем и пушим Docker‑образ
```bash
docker build -t your‑registry/flask-notes:latest .
docker push your‑registry/flask-notes:latest
```

# 3. Применяем k8s‑манифесты
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secret-mysql.yaml
kubectl apply -f k8s/pv-nfs.yaml
kubectl apply -f k8s/pvc-resource.yaml
kubectl apply -f k8s/mysql-statefulset.yaml
kubectl apply -f k8s/mysql-service.yaml
kubectl apply -f k8s/flask-deployment.yaml
kubectl apply -f k8s/flask-service.yaml
kubectl apply -f k8s/ingress.yaml
```
# 4. Проверяем статус
```bash
kubectl -n flask-notes-app get all
```