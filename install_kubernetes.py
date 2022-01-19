import os
from typing import List


class Kubernetes:
    command = ['sudo apt update -y',
               'wget –q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -',
               'sudo add-apt-repository "deb https://download.virtualbox.org/virtualbox/debian focal contrib"',
               'sudo apt-get install virtualbox -y',
               'curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"',
               'sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl -y',
               'kubectl version --client',
               'curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube',
               'sudo mkdir -p /usr/local/bin/ && sudo install minikube /usr/local/bin/',
               'minikube start --driver=virtualbox'
               ]
    for i in command:
        os.system(i)


