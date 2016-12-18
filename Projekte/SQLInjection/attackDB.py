#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import readline
import colors
import webbrowser


from generics import rlinput, execute, clearScreen

shellCols = colors.ShellColors

def open_FF(url):
	raw_input('Drücke ENTER um forzufahren.')
	webbrowser.open(url)
	#p = subprocess.Popen(["firefox", "http://localhost/select.html"])
	print(shellCols.WARNING + 'Web-Application in Firefox wurde gestartet...\n ' + shellCols.ENDC)

	#Schliessen der Web-Application & zurück zum Hauptmenü
	#raw_input('Drücke 0 um die Web-Application zu schliessen und das Tutorial zu beenden.')
	#p.kill()
	

def readFromDB():
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'SQL-Injection zum Auslesen von Daten: ' + shellCols.ENDC + '\n')

		#Öffnen der Web-Application
		print('Im ersten Teil des Tutorials werden mittels einer einfachen SQL-Injection Daten aus der DB gelesen, auf die man über die Anwendung eigentlich keinen Zugriff hätte.\n\nDazu wird eine Web-Application gestartet, in der die SQL-Injections durchgeführt werden können.\n')
		open_FF('http://localhost/sqlinjection/select.html')
	
		#Zum Hauptmenü zurück kehren
		selection = raw_input(shellCols.BLUE + '\nDrücke 0 um zum Menü zurückzukehren. ' + shellCols.ENDC)
		#print('Gehe zurück zum Hauptmenü')

		showMenu = False
		break

def insertToDB():
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'SQL-Injection zum Einfügen von Daten: ' + shellCols.ENDC + '\n')

		#Öffnen der Web-Application
		print('Im zweiten Teil des Tutorials wird mittels einer SQL-Injection ein zusätzlicher Datensatz in die Tabelle eingefügt. \n\nDazu wird eine Web-Application gestartet, in der die SQL-Injections durchgeführt werden können.\n')
		open_FF('http://localhost/sqlinjection/insert.html')
	
		#Zum Hauptmenü zurück kehren
		selection = raw_input(shellCols.BLUE + '\nDrücke 0 um zum Menü zurückzukehren. ' + shellCols.ENDC)
		#print('Gehe zurück zum Hauptmenü')

		showMenu = False
		break

def dropDB():
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'SQL-Injection zum Droppen der Tabelle: ' + shellCols.ENDC + '\n')

		#Öffnen der Web-Application
		print('Im dritten Teil des Tutorials wird mittels einer SQL-Injection die komplette Tabelle gelöscht (drop). Bitte beachte, dass du die Datenbank erst im Hauptmenü im Unterpunkt "5. Datenbank zurück setzen" wieder initialisieren musst, wenn du nach dem drop weiterarbeiten möchtest!\n\nDazu wird eine Web-Application gestartet, in der die SQL-Injections durchgeführt werden können.\n')
		open_FF('http://localhost/sqlinjection/drop.html')
	
		#Zum Hauptmenü zurück kehren
		selection = raw_input(shellCols.BLUE + '\nDrücke 0 um zum Menü zurückzukehren. ' + shellCols.ENDC)
		#print('Gehe zurück zum Hauptmenü')

		showMenu = False
		break

def playground():
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'SQL-Injections - Spielwiese :) ' + shellCols.ENDC + '\n')

		#Öffnen der Web-Application
		print('Innerhalb dieser Web-Application sind alle möglichen Statements noch einmal kurz aufgelistet. Hier kannst du testen, was du in den vorhergehenden Tutorials gelernt hast. \n\n')
		open_FF('http://localhost/sqlinjection/playground.html')
	
		#Zum Hauptmenü zurück kehren
		selection = raw_input(shellCols.BLUE + '\nDrücke 0 um zum Menü zurückzukehren. ' + shellCols.ENDC)
		#print('Gehe zurück zum Hauptmenü')

		showMenu = False
		break


