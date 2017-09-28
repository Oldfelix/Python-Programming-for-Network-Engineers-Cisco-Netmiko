#!/usr/bin/env python

import getpass
import telnetlib
import time
import os, sys

# Get Username and Password
password = getpass.getpass()
password2 = getpass.getpass()

# path to be created
path = "/var/www/html/jh/Development/python/workingscripts/switchconfigbk"

#  Open file with list of switches
f = open ("labswitches")

# Create directory for backup files
try:
    os.makedirs(path, 0755 );
except OSError:
    if not os.path.isdir(path):
        raise
#print("break and check folder creation")
print("Path has been created")
#time.sleep(5.5)

#  Telnet to each switch and cofigure it
for line in f:
	print "Getting running-config " + (line)
	HOST = line.strip()
	tn = telnetlib.Telnet(HOST)
        tn.read_until("Password: ")
        tn.write(password + "\n")
        tn.write("enable" + "\n")
        tn.read_until("Password: ")
        tn.write(password2 + "\n")
#        tn.write("conf t\n")
#        print ("Going into config t")
#        time.sleep(2.5) # pause 5.5 seconds
#        print ("Paused for 2.5 seconds for config t command")

	tn.write("terminal length 0\n")
	tn.write("show running-config\n")
	tn.write("exit\n")

        readoutput = tn.read_all()
        saveoutput =  open(path + "switch" + HOST, "w")
        saveoutput.write(readoutput)
        saveoutput.write("\n")
        saveoutput.close
        print tn.read_all()


