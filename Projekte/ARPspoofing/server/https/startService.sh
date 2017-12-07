#!/bin/bash

#generate private key
openssl genrsa -out /etc/ssl/private/apache.key 2048

#generate self-signed certificate
openssl req -new -x509 -key /etc/ssl/private/apache.key -days 365 -sha256 -out /etc/ssl/certs/apache.crt \
-subj "/C=DE/ST=Bayern/L=Ingolstadt/O=THI/OU=SecurityWorkBench/CN=thi.de"


#activate ssl modul
a2enmod ssl

#write ssl config file
cat << EOF > /etc/apache2/sites-available/ssl.conf
<VirtualHost *:443>
    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/apache.crt
    SSLCertificateKeyFile /etc/ssl/private/apache.key
    # Pfad zu den Webinhalten
    DocumentRoot /var/www/html/
</VirtualHost>
EOF

#activate VirtualHost
a2ensite ssl.conf

#start apache server
apachectl -D FOREGROUND

