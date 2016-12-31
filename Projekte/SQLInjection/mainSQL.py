#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import colors

import initializeDB
import attackDB

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
		print(shellCols.UNDERLINE + shellCols.HEADER + "SQL-Injection Tutorial" + shellCols.ENDC + '\n')
		print('Mit diesem Tutorial kannst du anhand eines praktischen Beispiels eine MySQL-Datenbank hacken. Genauere Informationen über das Thema SQL-Injection findest du im PDF-Handbuch der THI Security Workbench. In diesem Tutorial wirst du mittels einer SQL-Injection Daten aus der Datenbank auslesen, auf die du normalerweise keinen Zugriff haben solltest.\n')
		print('Die Datenbank inkl. User und DB-Schema wird zu Beginn des Tutorials oder durch das manuelle zurücksetzen immer wieder initialisiert. Dadurch kannst du auch direkt auf die Datenbank zugreifen und andere Szenarien ausprobieren.\n')
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Hauptmenü:' + shellCols.ENDC)
		print(shellCols.WARNING + "1.\tSQL-Injection zum Auslesen von Daten" + shellCols.ENDC)
		print(shellCols.WARNING + "2.\tSQL-Injection zum Einfügen von Daten" + shellCols.ENDC)
		print(shellCols.WARNING + "3.\tSQL-Injection zum Löschen von Tabellen" + shellCols.ENDC)
		print(shellCols.WARNING + "4.\tSQL-Injection - Spielwiese :)" + shellCols.ENDC)
		print(shellCols.WARNING + "5.\tDatenbank zurücksetzen" + shellCols.ENDC)
		print(shellCols.WARNING + "0.\tZurück zum Hauptmenü der Security-Workbench" + shellCols.ENDC)

		try:
			mainSelection = input(shellCols.BLUE + "\nDie Auswahl bitte hier eingeben und mit Enter bestätigen: " + shellCols.ENDC)
		except SyntaxError:
			mainSelection = 0
		if(mainSelection == 1):
			attackDB.readFromDB()
		elif(mainSelection == 2):
			attackDB.insertToDB()
		elif(mainSelection == 3):
			attackDB.dropDB()
		elif(mainSelection == 4):
			attackDB.playground()
		elif(mainSelection == 5):
			initializeDB.init()
		elif(mainSelection == 0):
			initializeDB.end_services()
			print("\nProgram beendet\n")
			showMenu = False
		else:
			print("\nNot valid!")

def sql_signal_handler(signal, frame):
	initializeDB.end_services()
	print('\n\n Die Security Workbench wird beendet ... \n')
	sys.exit(0)
