#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import subprocess

import colors
import generics
from generics import rlinput,execute,clearScreen,showCAPfiles,deauthClients

def Fake_Menu():
	attack = True
	while(attack==True):
		clearScreen()
		shellCols = colors.ShellColors
		print shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü: Fake-AP erstellen' + shellCols.ENDC +'\n'
		print("Mit Fake-APs versucht ein Angreifer einen WLAN-Nutzer dazu zu bringen, sich mit einer Kopie eines Original-Access-Points "
			+"zu verbinden und dann durch geschicktes Phishing Informationen von Nutzer zu erhalten. Im Idealfall merkt der Nutzer gar nicht, dass er mit "
			+"einem Fake-AP verbunden ist und er Opfer einer Phishing-Attacke wird. \n")
		print("Hinweis: Für dieses Tutorial werden zwei WLAN-Interfaces mit Packet-Injection-Unterstützung benötigt.")


		#START WIFIPHISHER
		command = rlinput('Starten von Wifiphisher und Durchführen des Angriffes: \n# ', 'wifiphisher')
		execute(command)
		
		#END
		print('Ende des Fake-AP-Tutorials erreicht! \n Bitte wählen zum Fortfahren: \n')
		print ('1. Zurück zum Menü \n'
			+ '2. Zurück zur Fake-AP-Übersicht\n' 
			+ '0. Tutorial beenden \n')
		try:
			selection = input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")
		except SyntaxError:
			selection=0
		if(selection==1):
			attack = False
			return True
		elif(selection==2):
			attack=True
			#Just du magic stuff. Unicorn!!
		else: 
			attack = False
			return False

	#FINISHED FAKEAP ATTACK
