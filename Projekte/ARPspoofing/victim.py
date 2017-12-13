#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import readline
import colors

from generics import rlinput, execute, clearScreen

def SniffingMode():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü Opfer der Darstellung des Netzwerkverkehrs: ' + shellCols.ENDC + '\n')

		##Schritt 1
		#TODO Was wird mit Host Netwerk gemeint
		print('Stelle im ersten Schritt sicher, dass du direkten Zugriff auf das Host-Netzwerk hast.\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 2
		# Hier vieleicht interactiver man kann ja auch ein netzwerk scan machen beim angrefeier und dann überprüfen ob sie überein stimmen
		command = rlinput('Rufe nun die Konfiguration deiner IP-Netzwerkschnittstellen auf und lies dort deine IP-Adresse aus: ', 'ifconfig')
		os.system(command)
		print('\n')

		##Schritt 3
		print('Als Zweites musst du deine ARP-Tabelle aufrufen, um sie ohne Manipulation zu sehen. ')
		command = rlinput('Das Aufrufen deiner ARP-Tabelle geht mit folgendem Befehl: ' , 'arp -a')
		os.system(command)
		print('\n')

		##Schritt 3
		print('Jetzt musst du warten, bis der Angreifer die Attacke durchgeführt hat.\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 4
		command = rlinput('Rufe noch einmal die ARP-Tabelle auf und vergleiche sie mit der vorherigen Tabelle: ', 'arp -a')
		os.system(command)
		print('\n')

		##Schritt 5
		selection = raw_input(shellCols.BLUE + '\nDrücke x um das Programm zu verlassen... ' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break

def ReplaceImagesMode():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü Opfer der Manipulation der Webseiten: ' + shellCols.ENDC + '\n')

		##Schritt 1
		print('Stelle im ersten Schritt sicher, dass du direkten Zugriff auf das Host-Netzwerk hast. Wie das geht, kannst du in der PDF-Dokumentation im Kapitel \"Tunneln von Netzwerkadaptern\" nachlesen.\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 2
		print('Rufe nun in deinem Browser die Homepage -  news.local - auf. Schliesse im Anschluss den Browser.')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt3
		print('Jetzt musst du warten bis der Angreifer seine Attacke durchgeführt hat.')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 4 
		print('Rufe nun in deinem Browser erneut die zuvor gewählte Webseite auf. Es sollte jetzt die Webseite manipuliert sein.')
		selection = raw_input(shellCols.BLUE + '\nDrücke x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		#if(selection == "x"):
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break
