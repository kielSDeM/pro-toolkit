    def qemu():
        command =['git clone https://gitlab.com/qemu-project/qemu.git; cd qemu',
                  'git submodule init; git submodule update --recursive','sudo apt-get install ninja-build',
                  'sudo apt-get install -y libglib2.0-dev; sudo apt-get install -y libpixman-1-dev',
                  'sudo apt-get install build-essential libcairo2-dev libpango1.0-dev libjpeg-dev libgif-dev librsvg2-dev',
                  'sudo apt-get install libavahi-ui-gtk3-dev', 'sudo apt install gtk-3-examples', 
                  'sudo apt install libguestfs-tools'
                 ]
        return command
