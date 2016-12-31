#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import readline

import colors
import WEP
import WPA
import DOS
import WPS
import Fake
import Enterprise
import generics

##########################################
# Main menu WIFI attacks
#########################################
def main():
	#JUST TO MAKE SHURE YOU ARE ROOT
	generics.RunAsRoot()

	showMenu = True

	while(showMenu):
		shellCols = colors.ShellColors
		#Main Menu
		generics.clearScreen()
		print shellCols.UNDERLINE + shellCols.ALTERNAHEADER + "WLAN-Netzwerk Tutorials" + shellCols.ENDC + '\n'
		print ('Dieses Tutorial bietet dem Benutzer die Möglichkeit, durch ein interaktives Skript, WLAN Passwörter für WEP und WPA/WPA2 zu knacken.'
			+' Ebenso können einige DoS-Attacken gegen WLAN-Netze interaktiv erlebt werden. Selbstverständlich dient dieses Tutorial nur einem '
			+'demonstrativen Zweck und es sollten nur WLAN-Netzwerke attackiert werden, die sich in einem isolierten Testumfeld befinden und der Nutzer '
			+'auch auf legalen Weg Zugriff hat. Im Tutorial selbst finden sich nur kurze Erklärungen zum Angriffverlauf. Für eine ausführliche '
			+'Erklärung wird zusammen mit diesem Tutorial eine Anleitung/Erklärung in .pdf-Form mitgeliefert.\n')
		print shellCols.UNDERLINE + shellCols.ALTERNAHEADER + "Main Menu" + shellCols.ENDC
		print shellCols.WARNING + "1.\tWEP-Key knacken" + shellCols.ENDC
		print shellCols.WARNING + "2.\tWPA/WPA2-PSK knacken" + shellCols.ENDC
		print shellCols.WARNING + "3.\tWLAN DoS-Attacken" + shellCols.ENDC
		print shellCols.WARNING + "4.\tWPS-PIN knacken" + shellCols.ENDC
		print shellCols.WARNING + "5.\tWPA/WPA2-Enterprise Passwort knacken" + shellCols.ENDC
		print shellCols.WARNING + "6.\tFake-AP erstellen" + shellCols.ENDC
		print shellCols.WARNING + "0.\tZurück zum Hauptmenü der Security-Workbench" + shellCols.ENDC
		try:
			mainSelection = input(shellCols.BLUE + "\nDie Auswahl bitte hier eingeben und mit Enter bestätigen: " + shellCols.ENDC)
		except SyntaxError:
			mainSelection = 0
		if(mainSelection == 1):
			showMenu =  WEP.WEP_Open()
		elif(mainSelection == 2):
			showMenu = WPA.WPA_Menu()
		elif(mainSelection == 3):
			showMenu = DOS.DOS_Menu()
		elif (mainSelection == 4):
			showMenu = WPS.WPS_Menu()
		elif (mainSelection == 5):
			showMenu = Enterprise.Enterprise_Menu()
		elif (mainSelection == 6):
			showMenu = Fake.Fake_Menu()
		elif(mainSelection == 0):
			showMenu = False

		if(showMenu == False):
			print "\nSkript wird beendet.\n"



def sql_signal_handler(signal, frame):
	print('\n\n Die Security Workbench wird beendet ... \n')
	sys.exit(0)
