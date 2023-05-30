#!/bin/bash
set -a
source local.env
set +a

read -p "is the docker image build? [y/n]: " input

if [[ $input =~ ^[Yy]$ ]]; then
  echo "Good Continuing..."
else
  echo "Sounds Good, building the docker image now..."

  docker build -t sonolacoca/nlp-fastapi-37-deployment:latest .
fi

echo "pushing the image to repository"

docker push sonolacoca/nlp-fastapi-37-deployment:latest


# Set the environment variables for the Docker CLI to use Minikube's Docker daemon
eval $(minikube docker-env)
echo "check the minikube status"

minikube status

read -p "is minikube already running? [y/n]: " input

if [[ $input =~ ^[Yy]$ ]]; then
  echo "Good Continuing..."
else
  echo "Sounds Good, starting minikube now..."

  minikube start
fi

# Set the current context to the Minikube cluster
kubectl config use-context minikube

# Create a deployment in the Kubernetes cluster using the specified Docker image
kubectl create deployment nlp-deployment --image=sonolacoca/nlp-fastapi-37-deployment:latest

# Create a service to expose the deployment
kubectl expose deployment nlp-deployment --type=LoadBalancer --port=${LOAD_BALANCER_PORT}

# Create a secret to store sensitive information
# NOTE: We might need in the future to utilize something like this
# kubectl create secret generic my-secret --from-literal=key1=value1 --from-literal=key2=value2

# Create a config map to store configuration data
kubectl create configmap config-from-localenv --from-env-file=local.env

kubectl apply -f nlp-api-manifest.yaml