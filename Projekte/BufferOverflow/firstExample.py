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
#		print('Schaue dir zuerst den Quellcode von FirstExample.c in einem TextEditor an und versuche nachzuvollziehen, was dort gemacht wird. Solltest du Hilfe benötigen, schau dir die Erklärung im PDF-Handbuch der THI Security Workbench in Kapitel Buffer Overflow an.\n')
#		command = rlinput('view BufferOverflow/FirstExample.c  \n')
#		execute(command)
#		command = rlinput('echo BufferOverflow/FirstExample.c')
#		os.system(command)
#		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
#		if(selection == "x"):
#			print('Gehe zurück zum Hauptmenü')
#			showMenu = False
#			break

		##Schritt 1
		print('Als erstes wollen wir den Quellcode zu einem ausführbaren Programm machen. ')
		command = rlinput('Dafür Kompilieren wir den Quellcode mit dem GNU Kompiler mit folgendem Befehl: ' , 'gcc -ggdb BufferOverflow/FirstExample.c -o BufferOverflow/FirstExample')
		os.system(command)
		print('\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 2
		print('Schaue dir nun den Quellcode von FirstExample.c in einem TextEditor an und versuche nachzuvollziehen, was dort gemacht wird. Solltest du Hilfe ben  tigen, schau dir die Erkl  rung im PDF-Handbuch der THI Security Workbench in Kapitel Buffer Overflow an.\n')
                command = rlinput('Um die Ansicht zu schliessen tippe ":quit" ein. ' ,'view BufferOverflow/FirstExample.c  \n')
                execute(command)
		print('\n')

		print('Jetzt wird der GNU Debugger in einem eigenen Terminal gestartet, um den Assembler Code des gerade eben erstellten Programms FirstExample zu debuggen. In diesem Terminal werden die Befehle gegeben, die zum Debuggen benutzt werden m  ssen.\n')
		command = rlinput('Starte den GNU Debugger mit folgendem Befehl: ' , 'gdb BufferOverflow/FirstExample')
		execute(command)
		print('\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurueck zum Hauptmenue')
			showMenu = False
			break

		##Schritt 3
		print('Öffne den Assembler Code der main-Funktion mit folgendem Befehl: disas main\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 4
		print('Versuche den Inhalt zu verstehen und ihn mit dem zuvor angeschauten Quellcode zu verknüpfen. Wichtig ist dabei herauszufinden, wie viele Stellen für den Eingabewert des Benutzers reserviert sind. Überschreitet man diesen Wert, wird das Passwort ausgegeben.\n')
		print('Schliesse nun die Assembler Ansicht mit folgendem Befehl: q\n')
		print('Schliesse dann den GNU Debugger mit folgendem Befehl: quit\n')	
		print('Beende das zweite Terminal mit dem Befehl: exit\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenue')
			showMenu = False
			break
		
		##Schritt 5
                print('Wir moechten nun genauer betrachten, welcher Bereich im Stack bei einer Uebergabe des Eingangsparameter, dafuer setzen wir einen Breakpoint bei Line 10 und bei Line 20 mit folgendem Befehl: break <Zeilennummer> \n')
                selection = raw_input(shellCols.BLUE + '\nDr  cke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zur  ck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 6
                print('Nun wird FirstExample gestartet mit folgendem Befgehl: run <Uebergabeparameter> z.B. run AAAAAAAA \n')
                selection = raw_input(shellCols.BLUE + '\nDr  cke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zur  ck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 7
                print('Es ist zu erkennen, dass das Programm beim ersten Breakpoint unterbrochen wurde und es wurde noch nicht der Uebergabeparameter im Stack abgelegt, deshalb schauen wir den Stack vorher genauer mit folgendem Befehl an: x/500b $sp \n')
                selection = raw_input(shellCols.BLUE + '\nDr  cke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zur  ck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 8
                print('Jetzt wird das Programm bis zum 2. Breakpoint fortgesetzt mit folgendem Befehl: continue \n')
                selection = raw_input(shellCols.BLUE + '\nDr  cke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zur  ck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 9
                print('Nun ist es Zeit sich nochmal den Stack genauer anzuschauen mit folgendem Befehl: x/500b $sp \n')
                selection = raw_input(shellCols.BLUE + '\nDr  cke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zur  ck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 10
                print('Abhaengig vom Uebergabeparameter ist nun der ASCI-Wert (dezimal) im Stack zu finden. \n')
                selection = raw_input(shellCols.BLUE + '\nDr  cke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zur  ck zum Hauptmen  ')
                        showMenu = False
                        break

		##Schritt 11
		print('Starte nun das ausfuehrbare Programm FirstExample aus dem Unterordner BufferOverflow und gib als Eingabewert einen String mit so vielen Stellen mit, dass das Passwort noch nicht mit ausgegeben wird.\n')
		command = rlinput('Starte FirstExample mit folgendem Befehl: ', './BufferOverflow/FirstExample <Deine Eingabe>')
		os.system(command)
		print('\n')

		##Schritt 12
		print('Starte nun das ausfuehrbare Programm FirstExample aus dem Unterordner BufferOverflow und gib als Eingabewert einen String mit so vielen Stellen mit, dass das Passwort mit ausgegeben wird.\n')
		command = rlinput('Starte FirstExample mit folgendem Befehl: ', './BufferOverflow/FirstExample <Deine Eingabe>')
		os.system(command)
		print('\n')

		##Schritt 13
		print('Das Tutorial ist hiermit beendet.\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke x um das Programm zu verlassen... ' + shellCols.ENDC)
		print('Gehe zurueck zum Hauptmenü')
		showMenu = False
		break
