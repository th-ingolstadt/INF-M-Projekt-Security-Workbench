#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import colors


import generics
import SYNFloodMain
import ICMPFlood


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
		print ('Dieses Tutorial bietet dem Benutzer die Möglichkeit, durch ein interaktives Skript, Denial of Service Attacken auszuführen.'
			+'Selbstverständlich dient dieses Tutorial nur einem demonstrativen Zweck.'
			+'Im Tutorial selbst finden sich nur kurze Erklärungen zum Angriffverlauf. Für eine ausführliche '
			+'Erklärung wird zusammen mit diesem Tutorial eine Anleitung in .pdf-Form mitgeliefert.\n')
		print shellCols.UNDERLINE + shellCols.ALTERNAHEADER + "Main Menu" + shellCols.ENDC
		print shellCols.WARNING + "1.\tICMP Flooding" + shellCols.ENDC
		print shellCols.WARNING + "2.\tSYN Flooding" + shellCols.ENDC
		print shellCols.WARNING + "0.\tZurück zum Hauptmenü der Security-Workbench" + shellCols.ENDC
		mainSelection = input(shellCols.BLUE + "\nDie Auswahl bitte hier eingeben und mit Enter bestätigen: " + shellCols.ENDC)
		if(mainSelection == 1):
			showMenu =  ICMPFlood.ICMP_MENU()
		elif(mainSelection == 2):
			showMenu = SYNFloodMain.main()
		elif(mainSelection == 0):
			showMenu = False

		if(showMenu == False):
			print "\nSkript wird beendet.\n"
