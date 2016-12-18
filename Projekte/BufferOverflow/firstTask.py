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
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü Buffer Overflow Aufgaben ' + shellCols.ENDC + '\n')

		##Schritt 1
		print('Versuche die beiden Aufgaben Buffer1 und Buffer2 aus dem Unterordner BufferOverflow selbstständig zu lösen. Starte zuerst ein neues Terminal, navigiere dich zum richtigen Ordner und gehe dann in der selben Reihenfolge vor, wie sie bei den beiden Beispielen vorgemacht wurde. Bei Problemen schau kurz ins PDF-Handbuch der Security Workbench. \n')

		##Schritt 2
		
		print('Das Tutorial ist hiermit beendet.\n')
		selection = raw_input(shellCols.BLUE + '\nDrücke x um das Programm zu verlassen... ' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break