#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import colors

import victim
import attacker
import sslstrip

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
		print(shellCols.UNDERLINE + shellCols.HEADER + "ARP Spoofing Tutorial" + shellCols.ENDC + '\n')
		print('Dieses Tutorial zeigt dir anhand eines praktischen Beispiels, wie eine ARP Spoofing Attacke ausgeführt wird. Genauere Informationen über das ARP Spoofing kannst du im PDF-Handbuch der THI Security Workbench finden. Das Tutorial ist zweigeteilt und zeigt dir im ersten Schritt, wie man einen Blick auf den Netzwerkverkehr anderer Geräte bekommen kann. Im zweiten Schritt werden die von anderen Geräten aufgerufenen Homepages durch den Austausch der vorkommenden Bilder manipuliert. \nACHTUNG: Dieses Tutorial darf nur in eigenen Netzwerken und zu Demonstrationszwecken verwendet werden!\n')
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Hauptmenü:' + 	shellCols.ENDC)
		print(shellCols.WARNING + "1.\tEinfaches ARP-Spoofing als Angreifer" + shellCols.ENDC)
		print(shellCols.WARNING + "2.\tStarte Darstellung des Netzwerkverkehrs als Opfer" + shellCols.ENDC)
		print(shellCols.WARNING + "3.\tARP-Spoofing und Verwendung von Filtern" + shellCols.ENDC)
		print(shellCols.WARNING + "4.\tStarte Manipulation der Bilddateien als Opfer" + shellCols.ENDC)
		print(shellCols.WARNING + "5.\tStarte SSLStrip Attacke als Angreifer" + shellCols.ENDC)
		print(shellCols.WARNING + "0.\tZurück zum Hauptmenü der Security-Workbench" + shellCols.ENDC)

		mainSelection = input(shellCols.BLUE + "\nDeine Auswahl: " + shellCols.ENDC)
		if(mainSelection == 1):
			attacker.SniffingMode()
		elif(mainSelection == 2):
			victim.SniffingMode()
		elif(mainSelection == 3):
			attacker.ReplaceImagesMode()
		elif(mainSelection == 4):
			victim.ReplaceImagesMode()
		elif(mainSelection == 5):
			sslstrip.Start()
		elif(mainSelection == 0):
			print("\nProgram beendet\n")
			showMenu = False
		else:
			print("\nUngültige Eingabe!")

