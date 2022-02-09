import os


class Programming:
    #installs the codium ide
    def codium(command):
        print("This class will install codium and snap on linux")
        command = ['sudo apt-get update',
                  'sudo apt-get install -y curl ; sudo apt-get install snapd',
                  'sudo snap install core ; sudo snap install codium --classic'
                  ]
        return command
    #installs python3
    def python3(command):
        print("going to install python3")
        command = ['sudo apt-get update',
                  'sudo apt install software-properties-common -y',
                  'sudo add-apt-repository ppa:deadsnakes/ppa',
                  'sudo apt install python3.10'
        return command
    #installs node.js
    def node_js(command):
        command = ['sudo apt-get update',
                   'sudo apt-get install python-software-properties',
                   'curl -fsSL https://deb.nodesource.com/setup_17.x | sudo -E bash -',
                   'sudo apt-get install nodejs',
                   'npm install -g npx']
        return command
      
    #installs miniconda
    def miniconda3(command):
        command = ['sudo apt update && sudo apt upgrade -y --allow-downgrade',
                   'mkdir -p ~/miniconda3', 'wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh',
                   'bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3',
                   'rm -rf ~/miniconda3/miniconda.sh', '~/miniconda3/bin/conda init bash',
                   '~/miniconda3/bin/conda init zsh', 'install miniconda']
    return command

    def pro(command):
        return command = [codium(command), pyhton3(command), nodejs(command), miniconda3(command)]
    
