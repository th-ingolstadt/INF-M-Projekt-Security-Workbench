#!/bin/bash
# Script to set LCD rotate and git clone 
# !!!! Keine Überprüfung ob schon konfiguriert durch mehrfaches ausführen geht die configuration kaputt !!!!

##Help Functions
#
#check if dpkg is locked
checkAPT() {
	while fuser /var/lib/dpkg/lock >/dev/null 2>&1 ; do
    		echo -en "\r Waiting for other software managers to finish..."
    		sleep 0.5
	done 
}
##
### Main 
#
## Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
##

echo "lcd_rotate=2" >> /boot/config.txt
apt update
apt install git
git clone https://github.com/th-ingolstadt/INF-M-Projekt-Security-Workbench
chown pi:pi -R INF-M-Projekt-Security-Workbench
##
## Keyboard layout
##
reboot
