#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import readline
import colors

from generics import rlinput, execute, clearScreen

def do():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü Erstes Buffer Overflow Beispiel ' + shellCols.ENDC + '\n')

		##Schritt 1
		print('Schaue dir zuerst den Quellcode von FirstExample.c in einem TextEditor an und versuche nachzuvollziehen, was dort gemacht wird. Solltest du Hilfe benötigen, schau dir die Erklärung im PDF-Handbuch der THI Security Workbench in Kapitel Buffer Overflow an.\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 2
		print('Als zweites wollen wir den Quellcode zu einem ausführbaren Programm machen. ')
		command = rlinput('Dafür Kompilieren wir den Quellcode mit dem GNU Kompiler mit folgendem Befehl: ' , 'gcc -ggdb BufferOverflow/FirstExample.c -o BufferOverflow/FirstExample')
		os.system(command)
		print('\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 3
		print('Jetzt wird der GNU Debugger in einem eigenen Terminal gestartet, um den Assembler Code des gerade eben erstellten Programms FirstExample zu debuggen. In diesem Terminal werden die Befehle gegeben, die zum Debuggen benutzt werden müssen.\n')
		command = rlinput('Starte den GNU Debugger mit folgendem Befehl: ' , 'gdb BufferOverflow/FirstExample')
		execute(command)
		print('\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 4
		print('Öffne den Assembler Code der main-Funktion mit folgendem Befehl: disas main\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 5
		print('Versuche den Inhalt zu verstehen und ihn mit dem zuvor angeschauten Quellcode zu verknüpfen. Wichtig ist dabei herauszufinden, wie viele Stellen für den Eingabewert des Benutzers reserviert sind. Überschreitet man diesen Wert, wird das Passwort ausgegeben.\n')
		print('Schließe nun die Assembler Ansicht mit folgendem Befehl: q\n')
		print('Schließe dann den GNU Debugger mit folgendem Befehl: quit\n')	
		print('Beende das zweite Terminal mit dem Befehl: exit\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break	

		##Schritt 6
		print('Starte nun das ausführbare Programm FirstExample aus dem Unterordner BufferOverflow und gib als Eingabewert einen String mit so vielen Stellen mit, dass das Passwort noch nicht mit ausgegeben wird.\n')
		command = rlinput('Starte FirstExample mit folgendem Befehl: ', './BufferOverflow/FirstExample <Deine Eingabe>')
		os.system(command)
		print('\n')

		##Schritt 7
		print('Starte nun das ausführbare Programm FirstExample aus dem Unterordner BufferOverflow und gib als Eingabewert einen String mit so vielen Stellen mit, dass das Passwort mit ausgegeben wird.\n')
		command = rlinput('Starte FirstExample mit folgendem Befehl: ', './BufferOverflow/FirstExample <Deine Eingabe>')
		os.system(command)
		print('\n')

		##Schritt 8
		
		print('Das Tutorial ist hiermit beendet.\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke x um das Programm zu verlassen... ' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break