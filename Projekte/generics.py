#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import readline

def rlinput(prompt, prefill=''):
	readline.set_startup_hook(lambda: readline.insert_text(prefill))
	try:
		return raw_input(prompt)
	finally:
		readline.set_startup_hook()

def execute(command):
	p = subprocess.Popen("x-terminal-emulator -e 'python execute.py " + command +"'", shell=True, stdout=subprocess.PIPE)


def monitor_mode(wifi_name):
	command = rlinput('WLAN-Interface in den Monitor-Mode versetzen: \n# ', 'airmon-ng start ' + wifi_name)
	execute(command)


def kill_wifi_proc():
	command = rlinput('Alle konkurrierende Prozesse Beenden, um aircrack-ng in vollem Umfang nutzen zu koennen: \n# ', 'airmon-ng check kill')
	execute(command)

def check_wifi_name(wifi_name):
	command = rlinput('Nach der Aktivierung des Monitor-Mode kann es vorkommen, dass das WLAN-Interface einen neuen Namen erhaelt. Den Interfacename pruefen mit: \n# ', 'ifconfig')
	execute(command)
	wifi_name_mon = raw_input("Falls sich der Name des Interfaces geaendert hat hier den Neuen angeben. (Falls keine Aenderungen Feld leer lassen.): ")
	if wifi_name_mon != "":
		wifi_name = wifi_name_mon

	return wifi_name

def deauthClients(router_bssid, wifi_name, text):
	command = rlinput(text, 'aireplay-ng --deauth 100 -a '+ router_bssid + ' ' + wifi_name)
	execute(command)

def clearScreen():
	os.system('cls' if os.name=='nt' else 'clear')

def showCAPfiles(router_ssid):
	print("")
	print("Zur nachfolgenden Analyse wird die aktuelle Netzwerkverkehraufnahmedatei benötigt. \n")
	print("Auswahl der neuesten *.cap Aufnahmedatei:")
	command = rlinput('# ', 'find ' + router_ssid +'-*.cap | awk \'{ if($1 > MAX) { MAX=$1} if(($1 < MIN) || MIN =="") {MIN = $1}} END{print MAX }\'' )
	p = subprocess.Popen(command , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()
	filenamestring = p.communicate()[0].strip()
	print ''
	print 'Folgende Datei wurde erkannt:'
	if(filenamestring==''):
		print "Keine passende CAP-Datei gefunden!"
		filenamestring= '<CAP-DATEINAME>'
	else:
		print filenamestring

	return filenamestring

def showSKA(name):
	print("")
	print("Zur Shared-Key-Fake-Authentication wird ein SKA-File benötigt. \n")
	print("Auswahl des neuesten SKA-Files:")
	command = rlinput('# ', 'find ' + name +'-*.xor | awk \'{ if($1 > MAX) { MAX=$1} if(($1 < MIN) || MIN =="") {MIN = $1}} END{print MAX }\'' )
	p = subprocess.Popen(command , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()
	filenamestring = p.communicate()[0].strip()
	print ''
	print 'Folgende Datei wurde erkannt:'
	if(filenamestring==''):
		print "Keine passende SKA-Datei gefunden!"
		filenamestring= '<SKA-DATEINAME>'
	else:
		print filenamestring

	return filenamestring


def stop_monitor_mode(wifi_name):
	command = rlinput('Anhalten des Monitor-Modes: \n# ', 'airmon-ng stop ' + wifi_name)
	execute(command)

def restart_networkmanager():
	command = rlinput('Neustart des Netzwerkmanagers: \n# ', 'service network-manager start')
	os.system(command)


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def find_replace_line (file_name, oldText, newText):
	f = open(file_name,'r')
	filedata = f.read()
	f.close()
	newdata = filedata.replace(oldText, newText)
	f = open(file_name,'w')
	f.write(newdata)
	f.close()

def check_string(file_name, text):
    if text in open(file_name).read():
    	return True
	return False

def append(file_name, text):
	f = open(file_name, 'a')
	f.write(text)


def RunAsRoot():
	if not os.geteuid() == 0:
		sys.exit('Bitte dieses Skript als Root ausführen.')

