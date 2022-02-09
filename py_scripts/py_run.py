from recon import Recon
from pro_py import Programming
from devops_kit import Dev_ops

#Can remove classes that you don't want to install.
class Main:
    print("this script will run through all installers")
    install = [pro(command), devops(command)]
    for i in install:
            os.system(i)
        break
    print('Programming languages and Devops tools.')

if __name__ == "__main__":
    Main()
