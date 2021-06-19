# build on online vscode
sudo apt-get purge python2.7-minimal -y
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install python3.6 python3-pip build-essential manpages-dev texlive-full fonts-noto-cjk -y
sudo ln -s /usr/bin/python3.6 /usr/bin/python
pip3 install cyaron