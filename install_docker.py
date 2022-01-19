import os


class Docker:
    command = ['sudo apt update && sudo apt upgrade -y --allow-downgrades',
               'sudo apt install docker.io -y',
               'systemctl start docker -y',
               'systemctl enable docker -y',
               'docker --version']
    for i in command:
        os.system(i)
