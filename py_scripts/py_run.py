from recon import Recon
from pro_py import Programming
from devops_kit import Dev_ops

#Can remove classes that you don't want to install.
class Main:
    print("this script will run through all install classes")
    install = [Recon(), Programming(), Dev_ops()]
    for i in install:
        install[i]
        break
    print('finished installing all scripts')

if __name__ == "__main__":
    Main()
