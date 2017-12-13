#!/bin/bash
# Script for Building Docker Container
# Build Docker Container
# ARP-Spoofing Container NEWS
project_path=$(realpath ..)

echo "ARP HTTP Webserver wird gebaut"
export ARP_WEB_RES_PATH=$project_path/ARPspoofing/server/http/html
chmod +x ../ARPspoofing/server/http/arphttpDockerControl.sh
../ARPspoofing/server/http/arphttpDockerControl.sh start

echo "ARP HTTPS Webserver wird gebaut"
# ARP-Spoofing Container HTTPS NO-HSTS
export ARP_WEB_RES_PATH=$project_path/ARPspoofing/server/https/html
chmod +x ../ARPspoofing/server/https/arphttpsDockerControl.sh
../ARPspoofing/server/https/arphttpsDockerControl.sh start

# ARP-Spoofing Container HTTPS HSTS
#export ARP_WEB_RES_PATH=$project_path/ARPspoofing/server/https/html
#chmod +x ../ARPspoofing/server/https/arphttpsDockerControl.sh
#../ARPspoofing/server/https/arphttpsDockerControl.sh start
echo "Tutorial Webseite wird gebaut"
# Tutorial Container 
export WEB_RES_PATH=$project_path/SecWorkbench/html
export WEB_RES_IP='172.26.112.1:80:80'
chmod +x ../SecWorkbench/tutorialDockerControl.sh
../SecWorkbench/tutorialDockerControl.sh start

# Linux Keylogger Container
export LINUX_KEYLOGGER_WEB_RES_PATH=$project_path/Keylogger/wifi_snatcher_DigiSpark/linux/html
../Keylogger/wifi_snatcher_DigiSpark/linux/keyloggerLinuxDockerControl.sh start
# Windows Keylogger container
export WINDOS_KEYLOGGER_WEB_RES_PATH=$project_path/Keylogger/wifi_snatcher_DigiSpark/windows/html
../Keylogger/wifi_snatcher_DigiSpark/windows/keyloggerDockerControl.sh start

echo "############################################################"
echo "Installion 2/2 Complete NO-Reboot needed."
echo "Info über WLAN-AP: NAME:PW"
echo "THISecurityWorkbenchWEPOpen/Share: BC6AFE583E"
echo "THISecurityWorkbenchWPA2: HackMeHackMe"
echo "THI SecurityWorkbenchWPA2-E: User: TestUser PW: HackMeHackMe"
echo "Genauere Informationen findet man in der Dokumentation"
echo "Webseiten Erreichbar unter: www.news.local, www.bank24.local"
echo "Tutorial ist nun erreichbar unter www.tutorial.local"
echo "Mit docker ps kann Ueberprueft werden ob die Container funktionieren"
docker ps
echo "############################################################"
