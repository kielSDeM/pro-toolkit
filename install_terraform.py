import os

class Terraform:
    def __init__(self, command):
        command.self = ['sudo apt update',
           'sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl',
           'curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -',
           'sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"',
           'sudo apt-get update && sudo apt-get install terraform',
           'terraform -help']

        for i in command.self:
                os.system(i)
