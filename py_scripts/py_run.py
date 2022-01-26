from recon import Recon
from recon import Alfa
from pro_py import Codium
from pro_py import Python3
from pro_py import MiniConda
from terraform_installer import Terraform

#Can remove classes that you don't want to install.
class Main:
    print("this script will run through all install classes")
    install = [Codium(), Recon(), Alfa(), Terraform(), Python3(), MiniConda()]
    for i in install:
        install[i]
        break
    print('finished installing all scripts')
