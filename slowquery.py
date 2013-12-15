#!/usr/bin/python

import os
import getpass
import sys


#### Check if slow-query.log exists, if yes remove
#### Search for database hostname
#### SSH to hostname 
#### sudo cp /var/logs/mysql/mysql-slow.log ~/
#### sudo chown $name:$group mysql-slow.log
#### mysqldumpslow -a -g $database mysql-slow | tee $database_slow.log
#### rm mysql-slow.log

#### try to do this all without asking for the password 3 times

#### SSH can have an assumed password, unsure if sudo can



## SUDOPASS = getpass.getpass("What is your password:  ")
WHOAMI = os.getlogin()

MYSQLSLOW = 'mysql-slow.log'

if len(sys.argv)>1:
	DATABASE = sys.argv[1]
	print(DATABASE)
else:
	print('Please include your database')
	sys.exit()

print('lets see if we get here')
