#!/bin/bash
#Script to install secWorkbench Kali-Linux
apt update && apt full-upgrade

## Get needed Packages for SecWorkbench
apt install ettercap-common hping3 arp-scan gdb okular reaver mdk3 hostapd-wpe hostapd metasploit-framework wifiphisher sslstrip psmisc dsniff

# disable lua to avoid lua warning for wireshark
wireshark_init_lua_line="disable_lua = false"
wireshark_init_lua_replacement="disable_lua = true"
sed -i.bak "s/${wireshark_init_lua_line}/${wireshark_init_lua_replacement}/g" /etc/wireshark/init.lua


## Generate SSH Keys
##
# Install Docker
apt-get install -y \
	apt-transport-https \
	ca-certificates \
	curl \
	gnupg2 \
	software-properties-common
# Add GPG Key 
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
# Add Source
echo "deb [arch=armhf] https://download.docker.com/linux/debian stretch stable" | sudo tee /etc/apt/sources.list.d/docker.list
# Update and install Docker-Comunitey Edition
apt-get update
apt-get install -y docker-ce
# Enable Docker on System Start
systemctl enable docker
service docker start 
# Create Docker container
#########################
project_path=$(realpath ..)
# Create DOS-Container
export DOS_WEB_RES_PATH=$project_path/DenialofService/server/html
../DenialofService/server/dosDockerControl.sh start
# Create Heartbleed-Container
#../Heartbleed/server/TODO
# Create Arp-Spoofing-Container
export ARP_WEB_RES_PATH=$project_path/ARPspoofing/server/http/html
../ARPspoofing/server/http/arphttpDockerControl.sh start
# Create SQLInjection-Container
export SQL_WEB_RES_PATH=$project_path/SQLInjection/html
../SQLInjection/server/sqlDockerControl.sh start

# Configurate SecWorkbench
#TODO Pfade Müssen gegebenfalls noch angepast werden
chmod +x ../WIFI/startFakeAP.sh

##Add OAth phising Need for wifiphisher 1.1
# git clone 
#tar xvfJ oauth-login.tar.xz /usr/lib/python2.7/dist-packages/wifiphisher/data/phishing-pages
# rm 
