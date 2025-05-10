# microservice-media-converter

push into the docker repo:

```sh
docker push zibizib/auth:tagname
```

```sh
# test
kubectl get pods
kubectl get services
kubectl get ingress
```

```sh
# don't forget this
# Stop any running tunnel first
pkill -f "minikube tunnel"

# Then start a new tunnel
minikube tunnel
```

```sh
# to run stuff i guess
# Get the ingress URL/IP
kubectl get ingress

# Or if using minikube
minikube service gateway --url
```
