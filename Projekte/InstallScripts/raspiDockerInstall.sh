#!/bin/bash
# Script for Building Docker Container
# Build Docker Container
# ARP-Spoofing Container NEWS
export ARP_WEB_RES_PATH='/home/pi/INF-M-Projekt-Security-Workbench/Projekte/ARPspoofing/server/http/html'
chmod +x ../ARPspoofing/server/http/arphttpDockerControl.sh
../ARPspoofing/server/http/arphttpDockerControl.sh start

# ARP-Spoofing Container HTTPS NO-HSTS
export ARP_WEB_RES_PATH='/home/pi/INF-M-Projekt-Security-Workbench/Projekte/ARPspoofing/server/https/html'
chmod +x ../ARPspoofing/server/https/arphttpsDockerControl.sh
../ARPspoofing/server/https/arphttpsDockerControl.sh start

# ARP-Spoofing Container HTTPS HSTS
#export ARP_WEB_RES_PATH='/home/pi/INF-M-Projekt-Security-Workbench/Projekte/ARPspoofing/server/https/html'
#chmod +x ../ARPspoofing/server/https/arphttpsDockerControl.sh
#../ARPspoofing/server/https/arphttpsDockerControl.sh start

# Tutorial Container 
export WEB_RES_PATH='/home/pi/INF-M-Projekt-Security-Workbench/Projekte/SecWorkbench/html'
export WEB_RES_IP='172.26.112.1:80:80'
chmod +x ../SecWorkbench/tutorialDockerControl.sh
../SecWorkbench/tutorialDockerControl.sh start
