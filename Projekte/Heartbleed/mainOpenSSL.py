#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import colors

import victim
import attacker

from generics import clearScreen

##########################################
# Show Menu
#########################################
def main():

	showMenu = True
	shellCols = colors.ShellColors

	while(showMenu):

		#Main Menu
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + "OpenSSL Heartbleed" + shellCols.ENDC + '\n')
		print('Es wird demonstriert, wie es aufgrund der Heartbleed Lücke in OpenSSL möglich war, Teile des Hauptspeichers des Servers auszulesen. Insbesondere wird versucht, den Private Key des Servers zu bestimmen.\n\nDie beiden Rollen können sowohl auf separaten Rechnern im selben Netz als auch auf einem Rechner gestartet werden. In letzterem Fall ist als IP-Adresse des Opfers/Servers die 127.0.0.1 zu verwenden.')
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Hauptmenü:' + 	shellCols.ENDC)
		print(shellCols.WARNING + "1.\tOpfer: Starte verwundbaren Server" + shellCols.ENDC)
		print(shellCols.WARNING + "2.\tAngreifer: Analyse und Angriff auf bereits gestarteten Server" + shellCols.ENDC)
		print(shellCols.WARNING + "0.\tZurück zum Hauptmenü der Security-Workbench" + shellCols.ENDC)

		mainSelection = input(shellCols.BLUE + "\nDeine Auswahl: " + shellCols.ENDC)
		if(mainSelection == 1):
			victim.ConfigureAndStartServer()
		elif(mainSelection == 2):
			attacker.StartHeartbleedMetasploit()
		elif(mainSelection == 0):
			print("\nProgram beendet\n")
			showMenu = False
		else:
			print("\nUngültige Eingabe!")

