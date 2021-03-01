# Implement Python Operator using Kopf

This project helps you bootstrap a Python Operator using KOPF.

## Description

Kopf stands for Kubernetes Operator Pythonic Framework.
For more information refer [kopf](https://kopf.readthedocs.io/en/stable/) 

## Getting Started

Clone the repo and follow below installation instructions.

### Installing

kubectl apply -f crd.yaml

kubectl get crd (now you should be able to see new CRD created)

docker image build -t simple-operator:latest .

kubectl apply -f service_account.yaml

kubectl apply -f service_account_binding.yaml

kubectl apply -f operator-deployment.yaml

kubectl get po (now you should see Operator POD deployed by Deployment)

kubectl apply -f resource.yaml

kubectl get deepak (now you should see new resource object created by name 'deepak' )

kubectl get pod (now you should be able to see new POD created by Operator with the name 'me')

kubectl delete -f dresource.yaml

kubectl get pod (now you should be able to see the POD by name 'me' deleted by Operator)
