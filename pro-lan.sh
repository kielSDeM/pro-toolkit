!#/bin/expect -f
echo "Hello this script is going to install codium and coding languages; also going to install spotify for some good vibes."
sudo apt update ; sudo apt upgrade -y
sudo apt-get dist-upgrade -y
sudo apt install -y curl
sudo apt install snapd
sudo snap install core ; sudo snap install spotify #music helps me code
sudo snap install codium --classic #my favorite ide.
echo "script is going to install your favorite programming languages!"
sudo apt install rustc
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
send "1\n"
sudo apt install npm -y ## Install NPM in the apt Repository
sudo npm install -g npm ## Update the NPM to Latest Stable version
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y nodejs 
npm install -g typescript -y
echo "npm version: "
npm -v
echo "node version: "
node --version
echo "Rust version: "
rustc --version
