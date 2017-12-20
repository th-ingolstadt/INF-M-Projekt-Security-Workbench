#!/bin/bash

# This script is meant to be run inside the container
# It will be run when the container starts up

# start apache2
#apachectl -D FOREGROUND
/etc/init.d/apache2 start
status=$?
if [ $status -ne 0 ]; then
	echo "ERROR: Could not start apache2: $status"
	exit $status
fi

# apache configuration
printf "RemoveHandler .html .htm \nAddType application/x-httpd-php .php .htm .html" >> /etc/apache2/apache2.conf

# start mysql
#/usr/bin/mysqld_safe
/etc/init.d/mysql start
status=$?
if [ $status -ne 0 ]; then
	echo "ERROR: Could not start mysql: $status"
	exit $status
fi

# create /var/run/mysqld/mysqld.sock file
touch /var/run/mysqld/mysqld.sock


# check if the DB initialize script was copied inside the container
if [ ! -f initializeDB.sql ]; then
	echo "DB initializing script missing!"
	exit 1
fi

# create DB
mysql -u root < initializeDB.sql
db_init_status=$?

if [ $db_init_status -ne 0 ]; then
	echo "DB creation failed!"
	exit $db_init_status
fi

#  regulary check the services
while /bin/true; do
	ps aux |grep apache |grep -q -v grep
	apache_status=$?
	ps aux |grep mysql |grep -q -v grep
	mysql_status=$?
	if [ $apache_status -ne 0 -o $mysql_status -ne 0 ]; then
		echo "Service error!"
		echo "MySQL status: $mysql_status"
		echo "apache status: $apache_status"
		exit 1
	fi
	sleep 60
done
