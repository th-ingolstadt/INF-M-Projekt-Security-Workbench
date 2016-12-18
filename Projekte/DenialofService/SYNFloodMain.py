#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import colors


import generics
import SYNFLOOD
import OpferSynFlood
import DeleteIPTable

##########################################
# Main menu DoS attacks
#########################################
def main():
	if not os.geteuid() == 0:
	    sys.exit('Bitte dieses Skript als Root ausführen.')

	showMenu = True

	while(showMenu):
		shellCols = colors.ShellColors
		#Main Menu
		generics.clearScreen()
		print shellCols.UNDERLINE + shellCols.ALTERNAHEADER + "Denial of Service(DoS) Tutorials" + shellCols.ENDC + '\n'
		print ('Dieses Tutorial bietet dem Benutzer die Möglichkeit, durch ein interaktives Skript, SYN-Flood Attacken auszuführen.\n')
		print shellCols.UNDERLINE + shellCols.ALTERNAHEADER + "SYN Flood Menu" + shellCols.ENDC
		print shellCols.WARNING + "1.\tAngreifer SYN Flooding" + shellCols.ENDC
		print shellCols.WARNING + "2.\tOpfer SYN Flooding" + shellCols.ENDC
		print shellCols.WARNING + "3.\tLöschen IP Tables Eintrag" + shellCols.ENDC
		print shellCols.WARNING + "0.\tZurück zum Hauptmenü der Security-Workbench" + shellCols.ENDC
		mainSelection = input(shellCols.BLUE + "\nDie Auswahl bitte hier eingeben und mit Enter bestätigen: " + shellCols.ENDC)
		if(mainSelection == 1):
			showMenu =  SYNFLOOD.SYNFLOOD_Menu()
		elif(mainSelection == 2):
			showMenu = OpferSynFlood.OpferSynFlood_Menu()
		elif(mainSelection == 3):
			showMenu = DeleteIPTable.DeleteIPTable_Menu()
		elif(mainSelection == 0):
			showMenu = False

		if(showMenu == False):
			print "\nSkript wird beendet.\n"
