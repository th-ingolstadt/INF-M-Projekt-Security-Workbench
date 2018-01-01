#!/bin/bash

# Dieses Startup-Skript startet alle benötigten Dienste für die Security Workbench

# Diese Zeilen werden nur für einen konfigurierten VSFTPD-Server benötigt.
# Hier dient der User webprouser als FTP-User, dessen Home-Verzeichnis mit dem Code-Verzeichnis der Security Workbench verknüpft wird.
#echo "Link ftp locations"
#mount --bind /home/webprouser/html/SecWorkbench/ /var/www/html/SecWorkbench/
#sudo chown -R www-data:www-data /var/www/html/
#echo ""

# build C programs
gcc -ggdb /var/www/html/SecWorkbench/App_Data/FirstExample.c -o /var/www/html/SecWorkbench/App_Data/FirstExample
gcc -ggdb /var/www/html/SecWorkbench/App_Data/SecondExample.c -o /var/www/html/SecWorkbench/App_Data/SecondExample

echo "Start docker..."
service docker start
service docker status | grep Active: | cut -ds -f1
echo ""

# Diese Zeilen sind nur dann relevant, wenn der FTP-Server vsftpd installiert wurde.
# Dieser dient zum Upload von Code für Entwickler, wenn die VM im Host only Netzwerk konfiguriert ist.
#echo "Start vsftpd..."
#service vsftpd start
#service vsftpd status | grep Active: | cut -ds -f1
#echo ""

path=/var/www/html/SecWorkbench/
export SQL_WEB_RES_PATH=$path
export WEB_RES_PATH=$path
echo "Web path = $WEB_RES_PATH"
echo ""

is_running="$(docker inspect -f {{.State.Running}} tutorialcontainer)"
if [ $is_running == "true" ]; then
	echo "tutorialcontainer is already running"
else
	echo "Start conainer..."
	'/root/Desktop/server/tutorialDockerControl.sh' start
fi
echo ""

echo "Use sudo chown -R webprouser:www-data /var/www/html/ when you update the web content via ftp."
echo "The ftp user webprouser with password root can be used to update the web content. When the update is done use sudo chown -R www-data:www-data /var/www/html/ to enable the webserver to access the web pages."
echo ""

ipAddr="$(ip addr show eth0 | grep 'inet' | cut -d: -f2 |cut -d/ -f1 | cut -dt -f2 | tr -d '[:space:]')"
echo "The webpage is available under: http://$ipAddr\SecWorkbench"


