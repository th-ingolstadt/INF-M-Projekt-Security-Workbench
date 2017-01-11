#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import readline
import colors

from generics import rlinput, execute, clearScreen



def ConfigureAndStartServer():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü Opfer/Server OpenSSL Heartbleed' + shellCols.ENDC + '\n')

		# Version
		print("OpenSSL ist eine Bibliothek rund um die Erzeugung von Zertifikaten und verschlüsselter Verbindungen. Die Versionen 1.0.1 bis einschließlich 1.0.1f waren von der Heartbleed-Lücke betroffen.\n\n")
		command = rlinput("Überprüfe die Version von OpenSSL: \n# ", "./openssl version")
		os.system(command)
		print('\n')

		# alte Files löschen
		try:
			os.remove("private_key.pem")
			os.remove("certificate.pem")
		except OSError:
			pass

		# Private Key und Zertifikat erstellen
		print("Für einen SSL-Server muss ein Private Key und ein Zertifikat erstellt werden. Die Angaben für die Zertifikatserstellung können freigelassen werden.\n\n")
		command = rlinput("Erzeuge Private Key und Zertifikat: \n# ", "./openssl req -x509 -newkey rsa:1024 -keyout private_key.pem -out certificate.pem -days 365 -nodes -config /etc/ssl/openssl.cnf")
		os.system(command)
		print('\n')

		# Private Key anzeigen
		print("Der erzeugte RSA Private Key kann mit OpenSSL Base64-kodiert angezeigt werden.\n\n")
		command = rlinput("Zeige Private Key an:\n# ", "./openssl rsa -in private_key.pem")
		os.system(command)
		print('\n')

		# Server starten
		print("Nun wird der verwundbare Server gestartet.\n\n")
		command = rlinput("Starte Server:\n# ", "./openssl s_server -key private_key.pem -cert certificate.pem -accept 8989 -www")
		execute(command)
		print('\n Der einfache Webserver kann nun auch im Browser unter https://localhost:8989 geöffnet werden. Es wird eine Info-Seite mit verfügbaren CipherSuites angezeigt.\n\n Nun kann der Angriff auf den Server gestartet werden.\n\n')


		##Beenden
		selection = raw_input(shellCols.BLUE + 'Drücke 0 um zum Menü zurückzukehren.' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break