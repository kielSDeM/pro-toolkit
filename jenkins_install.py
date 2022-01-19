import os


class Jenkins:
    command = ['minikube start',
               'minikube status',
               'kubectl create namespace jenkins',
               'kubectl get namespaces',
               'kubectl create -f jenkins-deployment.yaml -n jenkins',
               'kubectl get deployments -n jenkins',
               'kubectl create -f jenkins-service.yaml -n jenkins',
               'minikube ip',
               'kubectl get pods -n jenkins',
               ]
    for i in command:
        os.system(i)
