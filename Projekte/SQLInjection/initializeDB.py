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
	sqlDockerControl("start")
	return	

def end_services():
	# stop lamp container
	sqlDockerControl("stop")
	return
	
def sqlDockerControl( command ):
	curPath = os.path.dirname(os.path.realpath(__file__))
	webResourcePath = curPath + "/html"
	# restart container
	sqlControlScript = Popen(['/bin/bash', './SQLInjection/server/sqlDockerControl.sh', str(command)], env={"SQL_WEB_RES_PATH": webResourcePath})
	# wait until sqlControl script has finished
	sqlControlScript.communicate()
	# check exit status of the sqlControl script
	sqlControlScriptExitStatus = sqlControlScript.returncode
	if(0 != sqlControlScriptExitStatus):
		print("Error: sqlControl script returned", sqlControlScriptExitStatus)
		sys.exit(1)
	return

def init():
	# start/restart the lamp container
	sqlDockerControl("start")
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

