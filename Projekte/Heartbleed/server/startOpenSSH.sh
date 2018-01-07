#!/bin/bash

/local/bin/openssl version

/local/bin/openssl req -x509 -newkey rsa:1024 -keyout private_key.pem -out certificate.pem \
-days 365 -nodes -config /etc/ssl/openssl.cnf -subj "/C=DE/ST=Bayern/L=Ingolstadt/O=THI/OU=SecurityWorkBench/CN=thi.de"

/local/bin/openssl rsa -in private_key.pem

/local/bin/openssl  s_server -key private_key.pem -cert certificate.pem -accept 8989 -www


#Endlosschleifen für Testen
while true
do
   echo "In der Endlosschleife"
   sleep 5    # 5 Sekunden warten
done
