# flask-kuber
Сайт на http://note.mikop.su
# 1. Клонируем репозиторий
```bash
git clone http://github.com/app
cd app
```
# 2. Собираем и пушим Docker‑образ
```bash
docker build -t mikop/flask-notes:latest .
docker push mikop/flask-notes:latest
```
# 3. Установить NFS-CSI драйвер
```bash
helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm install csi-driver-nfs csi-driver-nfs/csi-driver-nfs --namespace kube-system
```
# 4. Применяем k8s‑манифесты
```bash
kubectl apply -f k8s/ -n flask-notes-app
```
Или:
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secret-mysql.yaml
kubectl apply -f k8s/nfs-server.yaml
kubectl apply -f k8s/storageclass-nfs-csi.yaml
kubectl apply -f k8s/pvc-resource.yaml
kubectl apply -f k8s/mysql-statefulset.yaml
kubectl apply -f k8s/mysql-service.yaml
kubectl apply -f k8s/flask-deployment.yaml
kubectl apply -f k8s/flask-service.yaml
kubectl apply -f k8s/ingress.yaml
```
# 5. Проверяем статус
```bash
kubectl -n flask-notes-app get all
```