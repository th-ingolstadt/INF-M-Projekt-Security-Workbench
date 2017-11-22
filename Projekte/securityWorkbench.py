#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import signal
import subprocess
import time
import readline


import colors
from WIFI import mainWIFI
from Heartbleed import mainOpenSSL
from ARPspoofing import mainARP
from SQLInjection import mainSQL
from BufferOverflow import mainBO
from DenialofService import mainDOS
import generics

##########################################
# Hauptmenü der Security-Workbench v1.0
#########################################
generics.RunAsRoot()

def default_signal_handler(signal, frame):
	print('\n\n Die Security Workbench wird beendet ... \n')
	sys.exit(0)


showMenu = True

while(showMenu):
	shellCols = colors.ShellColors
	# Main Menu
	subprocess.call(["clear"])

	# CTRL+C Handler reset
	signal.signal(signal.SIGINT, default_signal_handler)

	print shellCols.UNDERLINE + shellCols.HEADER + "Security-Workbench v1.1" + shellCols.ENDC + '\n'
	print ('Die Security-Workbench besteht im Kern aus zwei Elementen:\n')
	print (shellCols.UNDERLINE + 'Dokumentation als PDF-Dokument' +shellCols.ENDC + '\n'
		+'In der Dokumentation werden zum einen fachliche Grundlagen für ausgewählte Angriffsszenarien auf IT-Systeme vermittelt und zum anderen die Benutzung der Security-Workbench (Installation und Starten der Workbench sowie Arbeiten mit den Tools und Skripten) detailliert beschrieben.\n')
	print (shellCols.UNDERLINE + 'Skripte und Tools in einer Kali-Linux-Maschine' +shellCols.ENDC + '\n'
		+'Innerhalb einer virtuellen Kali-Linux-Maschine sind verschiedene Tools und Skripte hinterlegt. Mithilfe dieser Tools und Skripte können die in der PDF-Dokumentation erklärten Angriffsszenarien durchgespielt werden.\n')
	print ('Ziel der Security-Workbench ist es, Interessierten und Anfängern einen Einstiegspunkt zum Thema IT- Security zu geben. Daher ist es notwendig, die Bedienung und Dokumentation an den zu erwartenden Vorkenntnissen auszurichten.\n')
	print (shellCols.UNDERLINE + 'Disclaimer:' +shellCols.ENDC )
	print ("Alle hier gezeigten Tutorials sind ausschließlich für den Einsatz innerhalb einer eigens dafür geschaffenen Umgebung "
	+"(z.B. dediziertes WLAN zum Durchspielen der Angriffsszenarien) mit der Zustimmung aller Beteiligten (sowohl Angreifer als auch Angegriffene)"
	+" gedacht. Der Missbrauch der zur Verfügung gestellten Informationen und Tutorials für kriminelle Handlungen kann strafrechtliche "
	+"Folgen nach sich ziehen. Ausführliche Information befinden sich in der PDF-Dokumentation im Abschnitt \"Disclaimer\".")
	print shellCols.UNDERLINE + shellCols.HEADER + "Hauptmenü der Security-Workbench" + shellCols.ENDC
	print shellCols.WARNING + "1.\tPDF-Dokumentation öffnen" + shellCols.ENDC
	print shellCols.WARNING + "2.\tWLAN Tutorials" + shellCols.ENDC
	print shellCols.WARNING + "3.\tARP-Spoofing Tutorials" + shellCols.ENDC
	print shellCols.WARNING + "4.\tSQL-Injection Tutorials" + shellCols.ENDC
	print shellCols.WARNING + "5.\tOpenSSL Heartbleed" + shellCols.ENDC
	print shellCols.WARNING + "6.\tDenial of Service Tutorials" + shellCols.ENDC
	print shellCols.WARNING + "7.\tBuffer Overflow" + shellCols.ENDC
	print shellCols.WARNING + "0.\tTutorial beenden." + shellCols.ENDC
	try:
		mainSelection = input(shellCols.BLUE + "\nDie Auswahl bitte hier eingeben und mit Enter bestätigen: " + shellCols.ENDC)
	except SyntaxError:
		mainSelection = 0
	if(mainSelection == 1):
		file = '../Dokumentation/document.pdf'
		subprocess.Popen(["xdg-open", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	elif(mainSelection == 2):
		mainWIFI.main()
	elif(mainSelection == 3):
		mainARP.main()
	elif(mainSelection == 4):
		signal.signal(signal.SIGINT, mainSQL.sql_signal_handler)
		mainSQL.initializeDB.start_services()
		mainSQL.main()
	elif(mainSelection == 5):
		mainOpenSSL.main()
	elif(mainSelection == 6):
		mainDOS.main()
	elif(mainSelection ==7):
		mainBO.main()
	elif(mainSelection == 0):
		showMenu = False
	else:
		showMenu=False

	if(showMenu == False):
		print "\nSkript wird beendet.\n"


