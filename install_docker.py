import os


class Docker:
    command = ['sudo apt update && sudo apt upgrade -y --allow-downgrades',
               'sudo apt install docker.io',
               'systemctl start docker',
               'systemctl enable docker',
               'docker --version']
    for i in command:
        os.system(i)
