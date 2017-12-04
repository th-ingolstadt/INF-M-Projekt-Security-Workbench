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
		print('Schaue dir nun den Quellcode von FirstExample.c genau an und versuche nachzuvollziehen, was dort gemacht wird. Solltest du Hilfe benoetigen, schau dir die Erklaerung im PDF-Handbuch der THI Security Workbench in Kapitel Buffer Overflow an.\n')
                print('Nachdem du den Code verstanden hast, schliesse bitte mit ":quit" und anschliessend mit Enter. \n')
		command = rlinput('Mit dem folgendem Befehl wird FirstExample.c geoeffnet: ' ,'view BufferOverflow/FirstExample.c  \n')
                execute(command)	
		print('\n')
		print('Jetzt wird der GNU Debugger in einem eigenen Terminal gestartet, um den Assembler Code des gerade eben erstellten Programms FirstExample zu debuggen. In diesem Terminal werden die Befehle gegeben, die zum Debuggen benutzt werden muessen.\n')
		command = rlinput('Starte den GNU Debugger mit folgendem Befehl: ' , 'gdb BufferOverflow/FirstExample')
		execute(command)
		print('\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurueck zum Hauptmenue')
			showMenu = False
			break
		
		##Schritt 5
                print('Wir moechten nun genauer betrachten, welcher Bereich im Stack bei einer Uebergabe des Eingangsparameter, dafuer setzen wir einen Breakpoint bei Line 10 mit folgendem Befehl: break 10 \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 3
                print('Nun wird FirstExample gestartet mit folgendem Befehl: run <Uebergabeparameter> z.B. run AAAAAAAA ->Dez. von "A =65"\n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

	 	##Schritt 4
                print('Aus FirstExample.c war ersichtlich, dass das Ueberschreiben der Variable "authflag" zum gesuchten Loesungswort fuehrt. Das Ziehl ist es authflag zu beschreiben, deswegen moechten wir vorerst herausfinden, wo im Stack die Variable liegt.\n')
       	        print('\nMit folgendem Befehl wir sehen wir die Adresse der gesuchten Variable: print &authflag')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break		


		##Schritt 5
                print('Es ist ausserdem zu erkennen, dass das Programm beim Breakpoint unterbrochen wurde und noch nicht der Uebergabeparameter im Stack abgelegt wurde, deshalb schauen wir den Stack vorher genauer mit folgendem Befehl an: x/500b $sp \n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 6
                print('Mit folgendem Befehl wird das Programm um einen Schritt fortgesetzt: next \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break
			
                ##Schritt 7
                print('Nun ist es Zeit sich nochmal den Stack genauer anzuschauen mit folgendem Befehl: x/500b $sp \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 8
                print('Abhaengig vom Uebergabeparameter ist nun der ASCII-Wert (dezimal) im Stack zu finden. \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

		##Schritt 9
                print('Zaehle nun wie viele Stellen benoetigt werden, um die Variable "authflag" zu ueberschreiben \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break
			
		##Schritt 10
                print('Zaehle nun wie viele Stellen benoetigt werden, um die Variable "authflag" zu ueberschreiben \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break
		
		##Schritt 11
		print('Schliesse nun die Assembler Ansicht mit folgendem Befehl: quit und anschliessend mit Enter.\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenue')
			showMenu = False
			break
		
		##Schritt 12
		print('Starte nun das ausfuehrbare Programm FirstExample aus dem Unterordner BufferOverflow und gib als Eingabewert einen String mit so vielen Stellen mit, dass das Passwort noch nicht mit ausgegeben wird.\n')
		command = rlinput('Starte FirstExample mit folgendem Befehl: ', './BufferOverflow/FirstExample <Deine Eingabe>')
		os.system(command)
		print('\n')

		##Schritt 13
		print('Starte nun das ausfuehrbare Programm FirstExample aus dem Unterordner BufferOverflow und gib als Eingabewert einen String mit so vielen Stellen mit, dass das Passwort mit ausgegeben wird.\n')
		command = rlinput('Starte FirstExample mit folgendem Befehl: ', './BufferOverflow/FirstExample <Deine Eingabe>')
		os.system(command)
		print('\n')

		##Schritt 14
		print('Das Tutorial ist hiermit beendet.\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke x um das Programm zu verlassen... ' + shellCols.ENDC)
		print('Gehe zurueck zum Hauptmenü')
		showMenu = False
		break
