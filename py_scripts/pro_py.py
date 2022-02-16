class Programming:
    def __init__(self):
          self.install_list = []
    def __repr__(self):
        return self.install_list

    #installs the codium ide
    def codium(self):
        codium = ['sudo apt-get update',
                  'sudo apt-get install -y curl ; sudo apt-get install snapd',
                  'sudo snap install core ; sudo snap install codium --classic']

        return codium
    #installs python3
    def python3(self):
        py3 = ['sudo apt-get update',
                  'sudo apt install software-properties-common -y',
                  'sudo add-apt-repository ppa:deadsnakes/ppa',
                  'sudo apt install python3.10']
        
        return py3
    #installs node.js
    def node_js(self):
        node = ['sudo apt-get update',
                   'sudo apt-get install python-software-properties',
                   'curl -fsSL https://deb.nodesource.com/setup_17.x | sudo -E bash -',
                   'sudo apt-get install nodejs',
                   'npm install -g npx']
        return node

      
    #installs miniconda
    def miniconda3(self):
        mini = ['sudo apt update && sudo apt upgrade -y --allow-downgrade',
                   'mkdir -p ~/miniconda3', 'wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh',
                   'bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3',
                   'rm -rf ~/miniconda3/miniconda.sh', '~/miniconda3/bin/conda init bash',
                   '~/miniconda3/bin/conda init zsh', 'install miniconda']
        return mini
    def all(self):
        all = self.install_list
        all.extend(self.codium())
        all.extend(self.python3())
        all.extend(self.node_js())
        all.extend(self.miniconda3())
        
        return all