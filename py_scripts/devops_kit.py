import os


class Dev_ops:
    # installs terraform
    def terraform():
        command = ['sudo apt update; sudo apt upgrade -y',
                   'sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl',
                   'curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -',
                   'sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"',
                   'sudo apt-get update && sudo apt-get install terraform -y',
                   'terraform -help']
        for i in command:
            os.system(i)

    # installs minikube
    def mini_kube():
        command = ['curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64',
                   'sudo install minikube-linux-amd64 /usr/local/bin/minikube',
                   'sudo -E minikube start --driver=none',
                   'sudo minikube config set driver none']
        for i in command:
            os.system(i)
    # installs kubectl

    def kubectl():
        command = ['curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"',
                   'echo "$(<kubectl.sha256)  kubectl" | sha256sum --check',
                   'sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl']
    for i in command:
        os.system(i)
    # This installs jenkins on a minikube cluster

    def jenkins():
        command = ['minikube status',
                   'kubectl create -f jenkins-deployment.yaml -n jenkins',
                   'kubectl get deployments -n jenkins',
                   'kubectl create namespace jenkins',
                   'kubectl create -f jenkins-service.yaml -n jenkins']
        for i in command:
            os.system(i)

            
        # To access jenkins you need the pod name, cluster ip, and password:
        # minikube ip,
        # kubectl get pods -n jenkins
        # kubectl logs <pod_name> -n jenkins
        # The password can be found at the end of the logs
        # or you can use the path: /var/jenkins_home/secrets/initialAdminPassword
