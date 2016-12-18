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

def start_services():
	#Copy HTML/PHP files from git repository to apache2 source folder and start apache2
	srcdir = os.path.dirname(os.path.realpath(__file__)) + '/html'
	
	#####################################################################################
	############################# BEGIN OF CONFIGURATION ################################
	##### IN CASE YOU HAVE ANOTHER PATH TO APACHE2 WEBSERVER PLEASE CONFIGURE HERE ######
	#####################################################################################
	dstfile = '/var/www/html/sqlinjection.zip'
	dstdir = '/var/www/html/sqlinjection'
	#####################################################################################
	############################# END OF CONFIGURATION# #################################
	#####################################################################################
	
	#Delete existing directory and files sqlinjection in apache2-root
	shutil.rmtree(dstdir, ignore_errors=True)
	#Create necessary directories
	os.makedirs(dstdir)
	#Create Zip-File from git-repository and copy it to apache2-root
	#This way, the source-files from git can be modified an automaticly pushed into apache2 web servers
	shutil.make_archive(dstdir, 'zip', srcdir)
	
	#unzip sqlinjection.zip in apache2-root
	zip_ref = zipfile.ZipFile(dstfile, 'r')
	zip_ref.extractall(dstdir)
	zip_ref.close()

	#start apache2
	os.system('/etc/init.d/apache2 start')

	#start mysql
	os.system('/etc/init.d/mysql start')


def end_services():
	#shutdown apache 2
	os.system('/etc/init.d/apache2 stop')
	
	#shutdown mysql
	os.system('/etc/init.d/mysql stop')


def init():

	
	executeQuery('drop database if exists vulnerableDB;')
	executeQuery('create database vulnerableDB;')
	executeQuery('grant select, insert, update, delete, alter, drop, create on vulnerableDB.* to "normal_user"@"localhost" identified by "master42";')
	executeQuery('create table vulnerableDB.secretUserData(userId int primary key auto_increment, userName varchar(255), password varchar(30));')
	data = [
		('1', 'Douglas Adams', 'DontPanic!'),
		('2', 'Harry Potter', 'CaputDraconis'),
		('3', 'James T. Kirk', 'BeamMeUpScotty'),
		('4', 'Grumpy Cat', 'No!'),
		('5', 'Dalek', 'Exterminate!'),
		('6', 'The Doctor', 'Allons-y'),
		('7', 'Deadpool', 'Chimichanga')
	]
	insertIntoSecretUserData(data)

	print('Datenbank wurde zurueckgesetzt!')


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

