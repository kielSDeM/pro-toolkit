from terraform_installer import Terraform
from install_docker import Docker
from install_kubernetes import Kubernetes
from jenkins_install import Jenkins


#Can remove any of these classes if you don't want to use them.
Terraform()
Docker()
Kubernetes()
Jenkins()
