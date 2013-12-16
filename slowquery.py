#!/usr/bin/python

import os
import getpass
import sys
import paramiko

#### Check if slow-query.log exists, if yes remove
#### Search for database hostname
#### SSH to hostname 
#### sudo cp /var/logs/mysql/mysql-slow.log ~/
#### sudo chown $name:$group mysql-slow.log
#### mysqldumpslow -a -g $database mysql-slow | tee $database_slow.log
#### rm mysql-slow.log

#### try to do this all without asking for the password 3 times

#### SSH can have an assumed password, unsure if sudo can
debug = 0 
if debug == 1:
	help('modules')
	sys.exit()
else:
	print('nah')

## SUDOPASS = getpass.getpass("What is your password:  ")

#### Get user and the slow file
WHOAMI = os.getlogin()

MYSQLSLOW = 'mysql-slow.log'

#### If argv has more than 1 arguments set the variable, else end script
if len(sys.argv)>1:
	DATABASE = sys.argv[1]
	DBSLOW = DATABASE + "_slow.log"
	#print(DATABASE)
else:
	print('Please include your database')
	sys.exit()


#PATH Look for the database


SUDOPASS = getpass.getpass(WHOAMI + "'s Password: ")

connect = paramiko.SSHClient()

#connect.connect(username=WHOAMI, password=SUDOPASS) 

connect.load_system_host_keys()
connect.set_missing_host_key_policy(paramiko.WarningPolicy)

connect.connect('166.78.147.249', username=WHOAMI, password=SUDOPASS)

stdin, stdout, stderr = connect.exec_command('ls -al')
#for line in stdout.readlines():
#	print(line)

print(stdout.read())

#os.system("ssh " + WHOAMI + "@166.78.147.249" )
##print(DATABASE + " will be saved as " + DBSLOW)
##print('lets see if we get here')
