import os

class Codium:
    print("This class will install codium and snap on linux")
    codium = ['sudo apt-get update ; sudo apt-get upgrade -y',
              'sudo apt-get dist-upgrade -y', 
              'sudo apt-get install -y curl ; sudo apt-get install snapd',
              'sudo snap install core ; sudo snap install codium --classic'
              ]
    for i in codium:
        os.system(i)
    print("snap and codium are now installed.")

class Python3:
    print("going to install python3")
    python = ['sudo apt-get update && sudo apt-get upgrade -y',
              'sudo apt install software-properties-common -y', 
              'sudo add-apt-repository ppa:deadsnakes/ppa', 
              'sudo apt install python3.10']
    for i in python:
        os.system(i)
    print("python3 is now installed")

class MiniConda:
    print("installing miniconda3")
    command = ['sudo apt update && sudo apt upgrade -y --allow-downgrade',
               'mkdir -p ~/miniconda3', 'wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh',
               'bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3',
               'rm -rf ~/miniconda3/miniconda.sh', '~/miniconda3/bin/conda init bash',
               '~/miniconda3/bin/conda init zsh', 'install miniconda']

    for i in command:
                   os.system(i)
    print("installation is now complete!")

