#!/usr/bin/python
import os
import sys
import subprocess
import time
import readline
import colors
import shutil
import zipfile

from generics import rlinput, execute, clearScreen
from subprocess import Popen

def start_services():
	# start lamp docker container
	lampControl("start")
	return	

def end_services():
	# stop lamp container
	lampControl("stop")
	return
	
def lampControl( command ):
	curPath = os.path.dirname(os.path.realpath(__file__))
	webResourcePath = curPath + "/html"
	# restart container
	lampControlScript = Popen(['/bin/bash', './SQLInjection/server/lampDockerControl.sh', str(command)], env={"WEB_RES_PATH": webResourcePath})
	# wait until lampControl script has finished
	lampControlScript.communicate()
	# check exit status of the lampControl script
	lampControlScriptExitStatus = lampControlScript.returncode
	if(0 != lampControlScriptExitStatus):
		print("Error: lampControl script returned", lampControlScriptExitStatus)
		sys.exit(1)
	return

def init():
	# start/restart the lamp container
	lampControl("start")
	print('Datenbank wurde zurueckgesetzt!')
	return

def executeQuery( query ):
	import MySQLdb as mdb
	ROOT_USER = 'root'
	ROOT_PW = ''
	print query

	try:
		con = mdb.connect('localhost', ROOT_USER, ROOT_PW)
		cur = con.cursor()
		cur.execute(query)
	except mdb.Error, e:
		print "Error %d: %s" %(e.args[0], e.args[1])
		sys.exit[1]
	finally:
		if con:
			con.close()
	return

def insertIntoSecretUserData( data ):
	import MySQLdb as mdb
	ROOT_USER = 'root'
	ROOT_PW = ''

	try:
		con = mdb.connect('localhost', ROOT_USER, ROOT_PW)
		cur = con.cursor()
		cur.executemany('insert into vulnerableDB.secretUserData values(%s, %s, %s);', data)
	except mdb.Error, e:
		print "Error %d: %s" %(e.args[0], e.args[1])
		sys.exit[1]
	finally:
		if con:
			con.commit()
			con.close()
	return

