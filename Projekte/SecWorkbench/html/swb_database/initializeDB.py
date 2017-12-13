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

	executeQuery('create table vulnerableDB.xssGuestbook(User varchar(20), Date date, comment varchar(255));')
	xss_data = [
		('admin', '2017-11-15', 'Guten Tag! Es freut mich sehr, dass ich hiermit den ersten Beitrag in unserem Gästebuch erstellen darf und möchte dich herlich Willkommen heißen! :)'),
		('admin', '2017-11-15', 'Was wohl mit diesem stored cross site scripting ales möglich ist'),
		('admin', '2017-11-16', 'Wenn ich an Cookies denke, dann frage ich mich manchmal was dort drin steht.. manchmal hab ich auch einfach nur Lust auf einen Cookie :D'),
		('Mr. Robot', '2017-11-18', '42'),
		('root', '2017-11-20', 'Hello World!'),
		('root', '2017-11-21', '1 + 1 = 0'),
		('Mr. Robot', '2017-11-22', 'Knock, knock. Race condition. Who’s there.'),
		('Mr. Robot', '2017-11-25', 'Why do Java programmers wear glasses? Because they don’t C#!')
	]
	insertDataIntoGivenTable(xss_data, xssGuestbook)

	executeQuery('create table vulnerableDB.sqlInjectionRanking(userid int primary key auto_increment, user varchar(20), punkte int);')
	sqlInjectionModifyData = [
		('1', 'Daniel', '50'),
		('2', 'Werner', '77'),
		('3', 'Mr. Robot', '66'),
		('4', 'Bernd', '44'),
		('5', 'root', '42'),
		('6', 'admin', '99'),
		('7', 'Mr. Universe', '39'),
		('8', 'Kaaarl', '13'),
		('9', 'Bernd', '17'),
		('10', 'Kevin', '0'),
		('11', 'pr0xy', '10'),
		('12', '4c1d', '29'),
		('13', '6r1ff1n', '6r1ff1n'),
		('14', 'n3m3515', '21')
		('15', 'Bu5yB34ver', '81')
	]
	insertDataIntoGivenTable(sqlInjectionModifyData, sqlInjectionRanking)

	executeQuery('create table vulnerableDB.cookieManagementUsers(userid int primary key auto_increment, username varchar(255) not null, password varchar(255) not null);')
	cookieManagementData[
		('1', 'admin', 'admin'),
		('2', 'user', 'hallo123'),
		('3', 'benutzer', 'passwort1'),
		('4', 'fußballfan', 'schalke04'),
		('5', 'test', 'test'),
		('6', 'master', 'master'),
		('7', 'system', 'system123'),
		('8', 'superuser', 'super'),
		('9', 'administrator', '11111'),
		('10', 'account' , 'abcd'),
		('11', 'benutzerkonto', 'benutzer'),
		('12', 'superman', '123456'),
		('13', 'mr.robot', 'hacker'),
		('14', 'biene', 'maja'),
		('15', 'test1', 'password')
	]
	insertDataIntoGivenTable(cookieManagementData, cookieManagementUsers)

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

def insertDataIntoGivenTable( data, tableName ):
	import MySQLdb as mdb
	ROOT_USER = 'root'
	ROOT_PW = ''

	try:
		con = mdb.connect('localhost', ROOT_USER, ROOT_PW)
		cur = con.cursor()
		query = 'insert into vulnerableDB.' + tableName + ' values(%s, %s, %s);';
		cur.executemany(query, data)
	except mdb.Error, e:
		print "Error %d: %s" %(e.args[0], e.args[1])
		sys.exit[1]
	finally:
		if con:
			con.commit()
			con.close()
	return
