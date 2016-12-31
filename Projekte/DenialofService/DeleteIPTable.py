#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import subprocess
import colors
import generics
from generics import rlinput, execute, clearScreen

def DeleteIPTable_Menu():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print shellCols.UNDERLINE + shellCols.HEADER + 'Löschen der IP-Tables Einträge' + shellCols.ENDC + '\n'
		
		#IP Adressen Opfer/Angreifer
		print('Zuerst muss die IP-Adresse des zuvor benutzten Interfaces angegeben werden.')
		command = rlinput('Anzeigen der Interfaces mit folgendem Befehl: \n# ', 'ifconfig')
		execute(command)

		ipadr = rlinput('Eigene IP-Adresse(IPv4: ')
		
		command = rlinput('IP-Tables-Eintrag: \n# ', 'iptables -D OUTPUT -p tcp -s ' +ipadr + ' --tcp-flags RST RST -j DROP')
		os.system(command)
		print('\n')


		selection = raw_input(shellCols.BLUE + '\nDrücke x um das Programm zu verlassen...' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break
