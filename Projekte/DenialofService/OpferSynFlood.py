#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import subprocess
import colors
import generics
from generics import rlinput, execute, clearScreen

def OpferSynFlood_Menu():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print shellCols.UNDERLINE + shellCols.HEADER + 'Opfer SYN-Flooding' + shellCols.ENDC + '\n'
		
		#Apache2 server starten
		print('In diesem Abschnitt wird der Apache2-Server gestartet, der im SYN-Flooding-Tutorial angegriffen wird.')
		command = rlinput('Der Server wird mit folgendem Befehl gestartet: \n# ', ' /etc/init.d/apache2 start')
		os.system(command)
		print('\n')

		#IP Adressen Opfer/Angreifer
		print('Zuerst muss die IP-Adresse des Interfaces angegeben werden, welches mit dem Netzwerk verbunden ist.')
		command = rlinput('Anzeigen der Interfaces mit folgendem Befehl: \n# ', 'ifconfig')
		execute(command)
		
		ipVictim = raw_input('Bitte die eigene IP-Adresse(IPv4) eingeben: ')
		ipAttacker = raw_input('Bitte die IP-Adresse(IPv4) des Angreifers eingeben: ')
 		
		
		print('Der folgende Ausdruck zeigt in Wireshark alle Einträge mit beiden IP-Adressen: ')
		print('ip.addr == ' +ipVictim + ' && ip.addr == ' +ipAttacker)
		
		

	 	selection = raw_input(shellCols.BLUE + '\nDrücke ENTER um den Server zu stoppen. Führen sie diesen Befehl nur aus, wenn die Attacke bereits beendet wurde. ' + shellCols.ENDC)
		command = rlinput('Der Server wird mit folgendem Befehl gestoppt : \n# ', ' /etc/init.d/apache2 stop')
		os.system(command)
		selection = raw_input(shellCols.BLUE + '\nDrücke ENTER um das Programm zu verlassen...' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break
