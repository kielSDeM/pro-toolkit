import os
from recon import Recon
from pro_py import Programming
from devops_kit import Dev_ops

#Can remove classes that you don't want to install.
class Main:
    pro = Programming()
    dev = Dev_ops()
    pro_dev = []
    pro_dev.extend(pro.all())
    pro_dev.extend(dev.all_dev())
    
    for i in pro_dev:
            os.system(i)

if __name__ == "__main__":
    Main()
