#!/bin/sh
# 2011-11-10 followed these steps on ts130
# on the chef server
deb http://apt.opscode.com/ lucid-0.10 main
echo "deb http://apt.opscode.com/ `lsb_release -cs`-0.10 main" | sudo tee /etc/apt/sources.list.d/opscode.list
gpg --keyserver keys.gnupg.net --recv-keys 83EF826A
gpg --export packages@opscode.com | sudo tee /etc/apt/trusted.gpg.d/opscode-keyring.gpg > /dev/null
sudo apt-get install opscode-keyring # permanent upgradeable keyring
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install chef chef-server -y # is chef necessary? also, this'll prompt you for the webui and rabbitmq passwords (use alphanumeric only)
mkdir -p ~/.chef
sudo cp /etc/chef/validation.pem /etc/chef/webui.pem ~/.chef
sudo chown -R $USER ~/.chef
knife configure -i # set server url to localhost:4000 and client name to CLIENT-ID
knife client list
knife client create CLIENT-ID -n -a -f /tmp/CLIENT-ID.pem

# on the chef client
deb http://apt.opscode.com/ lucid-0.10 main
echo "deb http://apt.opscode.com/ `lsb_release -cs`-0.10 main" | sudo tee /etc/apt/sources.list.d/opscode.list
gpg --keyserver keys.gnupg.net --recv-keys 83EF826A
gpg --export packages@opscode.com | sudo tee /etc/apt/trusted.gpg.d/opscode-keyring.gpg > /dev/null
sudo apt-get install opscode-keyring
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install chef
mkdir ~/.chef
sudo mkdir /etc/chef
sudo scp referid.co:/etc/chef/validation.pem /etc/chef
scp referid.co:/tmp/CLIENT-ID.pem ~/.chef/CLIENT-ID.pem
sudo mkdir /etc/chef
knife configure -i # set server url to referid.co:4000
knife client list
