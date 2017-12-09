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
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü Zweites Buffer Overflow Beispiel ' + shellCols.ENDC + '\n')

		##Schritt 1
		print('Als erstes wollen wir den Quellcode zu einem ausführbaren Programm machen. ')
		command = rlinput('Dafür Kompilieren wir den Quellcode mit dem GNU Kompiler mit folgendem Befehl: ' , 'gcc -ggdb BufferOverflow/SecondExample.c -o BufferOverflow/SecondExample')
		os.system(command)
		print('\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurück zum Hauptmenü')
			showMenu = False
			break

		##Schritt 2
		print('Schaue dir nun den Quellcode von SecondExample.c genau an und versuche nachzuvollziehen, was dort gemacht wird. Solltest du Hilfe benoetigen, schau dir die Erklaerung im PDF-Handbuch der THI Security Workbench in Kapitel Buffer Overflow an.\n')
                print('Nachdem du den Code verstanden hast, schliesse bitte mit ":quit" und anschliessend mit Enter. \n')
		command = rlinput('Mit dem folgendem Befehl wird SecondExample.c geoeffnet: ' ,'view BufferOverflow/SecondExample.c  \n')
                execute(command)	
		print('\n')
		print('Jetzt wird der GNU Debugger in einem eigenen Terminal gestartet, um den Assembler Code des gerade eben erstellten Programms SecondExample zu debuggen. In diesem Terminal werden die Befehle gegeben, die zum Debuggen benutzt werden muessen.\n')
		command = rlinput('Starte den GNU Debugger mit folgendem Befehl: ' , 'gdb BufferOverflow/SecondExample')
		execute(command)
		print('\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
		if(selection == "x"):
			print('Gehe zurueck zum Hauptmenue')
			showMenu = False
			break
		
		##Schritt 3
                print('Wir moechten nun genauer betrachten, welcher Bereich im Stack veraendert wird bei einer Uebergabe des Eingangsparameter. Deshalb setzen wir einen Breakpoint bei Line 10 mit folgendem Befehl: break 10 \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 4
                print('Nun wird SecondExample gestartet mit folgendem Befehl: run <Uebergabeparameter> z.B. run AAAAAAAA ->Dez. von "A =65"\n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

	 	##Schritt 5
                print('Aus SecondExample.c ist ersichtlich, dass das Ueberschreiben der Variable "authflag" zum gesuchten Loesungswort fuehrt, jedoch faellt die zusaetzliche Variable "checkForHack" auf (warum?). Das Ziel ist wie bei FirstExample "authflag" zu uebeschreiben, deswegen moechten wir vorerst herausfinden, wo im Stack die Variable zu finden ist.\n')
		print('\nMit folgendem Befehl sehen wir die Startadresse der Eingabe-Variable "buffer": print &buffer')
		print('\nMit folgendem Befehl sehen wir die Adresse der gesuchten Variable: print &authflag')
		print('\nMit folgendem Befehl sehen wir die Adresse der zusaetzlich aufgetauchten Variable: print &checkForHack')
		print('\nMache dir gedanken, welchen Einfluss die Variable "checkForHack", im zusammenhang mit der dazugehörigen Adresse im Stack, hat.')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break		


		##Schritt 6
                print('Es ist ausserdem zu erkennen, dass das Programm beim Breakpoint unterbrochen wurde und der Uebergabeparameter im Stack noch nicht abgelegt wurde, deshalb schauen wir den Stack mit folgendem Befehl vorher genauer an: x/500b $sp \n')
		selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 7
                print('Mit folgendem Befehl wird das Programm um einen Schritt fortgesetzt: next \n')
		print('Der Uebergabeparameter wird daraufhin im Stack abgelegt.\n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break
			
                ##Schritt 8
                print('Nun ist es Zeit, den Stack mit folgendem Befehl nochmal genauer anzuschauen: x/500b $sp \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

                ##Schritt 9
                print('Abhaengig vom Uebergabeparameter ist nun der ASCII-Wert (dezimal) im Stack zu finden. \n')
                selection = raw_input(shellCols.BLUE + '\nDruecke Enter um fortzufahren oder x um das Programm zu verlassen... ' + shellCols.ENDC + '\n')
                if(selection == "x"):
                        print('Gehe zurueck zum Hauptmen  ')
                        showMenu = False
                        break

		##Schritt 10
                print('Zaehle oder berechne, anhand der vorher angezeigten Adressen, nun wie viele Stellen benoetigt werden, um die Variable "authflag" zu ueberschreiben und tippe "q" ein. \n')
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
		print('Starte nun das ausfuehrbare Programm SecondExample aus dem Unterordner BufferOverflow und gib als Eingabewert einen String mit so vielen Stellen mit, dass die Daten des Bankkunden noch nicht mit ausgegeben werden.\n')
		command = rlinput('Starte SecondExample mit folgendem Befehl: ', './BufferOverflow/SecondExample <Deine Eingabe>')
		os.system(command)
		print('\n')

		##Schritt 13
		print('Starte nun das ausfuehrbare Programm SecondExample aus dem Unterordner BufferOverflow und gib als Eingabewert einen String mit so vielen Stellen mit, dass die Daten des Bankkunden mit ausgegeben werden.\n')
		command = rlinput('Starte SecondExample mit folgendem Befehl: ', './BufferOverflow/SecondExample <Deine Eingabe>')
		os.system(command)
		print('\n')
		print('Warum hat die anscheinend richtige Eingabe nicht zum gewuenschten Ergebnis gefuehrt?\n')

		##Schritt 14
		print('Das Tutorial ist hiermit beendet.\n')
		selection = raw_input(shellCols.BLUE + '\nDruecke x um das Programm zu verlassen... ' + shellCols.ENDC)
		print('Gehe zurueck zum Hauptmenü')
		showMenu = False
		break
