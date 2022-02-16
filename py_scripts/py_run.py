from recon import Recon
from pro_py import Programming
from devops_kit import Dev_ops

#Can remove classes that you don't want to install.
class Main:
    pro = Programming()
    dev = Dev_ops()
    install = [pro.all(), dev.all_dev()]
    for i in len(install):
            os.system(i)
    print('Programming languages and Devops tools.')

if __name__ == "__main__":
    Main()
