#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import colors
import firstExample
import secondExample
import firstTask

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
		print(shellCols.UNDERLINE + shellCols.HEADER + "BufferOverflow Tutorial" + shellCols.ENDC + '\n')
		print('Dieses Tutorial zeigt dir anhand eines praktischen Beispiels, wie eine Buffer Overflow Attacke ausgeführt wird. Genauere Informationen über Buffer Overflow kannst du im PDF-Handbuch der THI Security Workbench finden. Das Tutorial besitzt zwei kleine Beispiele, an denen nachvollzogen werden kann, was gemacht werden muss. Danach kannst du selbst ausprobieren, ob du die beiden anderen Aufgaben lösen kannst. Die Aufaben sind dabei ähnlich aufgebaut, wie die Beispiele, so dass nach dem gleichen Prinzip vorgegangen werden kann.')
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Hauptmenü:' + 	shellCols.ENDC)
		print(shellCols.WARNING + "1.\tErstes Beispiel" + shellCols.ENDC)
		print(shellCols.WARNING + "2.\tZweites Beispiel" + shellCols.ENDC)
		print(shellCols.WARNING + "3.\tEigene Aufgaben" + shellCols.ENDC)
		print(shellCols.WARNING + "0.\tZurück zum Hauptmenü der Security-Workbench" + shellCols.ENDC)

		mainSelection = input(shellCols.BLUE + "\nDeine Auswahl: " + shellCols.ENDC)
		if(mainSelection == 1):
			firstExample.do()
		elif(mainSelection == 2):
			secondExample.do()
		elif(mainSelection == 3):
			firstTask.do()
		elif(mainSelection == 0):
			print("\nProgram beendet\n")
			showMenu = False
		else:
			print("\nUngültige Eingabe!")

