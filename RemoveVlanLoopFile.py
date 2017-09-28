#!/usr/bin/env python

import getpass
import sys
import telnetlib
import time
password = getpass.getpass()
password2 = getpass.getpass()


f = open ('labswitches')

for line in f:
    print "Configuring Switch " + (line)
    HOST = line
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Password: ")
    tn.write(password + "\n")
    tn.write("enable" + "\n")
    tn.read_until("Password: ")
    tn.write(password2 + "\n")
    tn.write("conf t\n")
    print ("Going into config t")
    time.sleep(1.5) # pause 5.5 seconds
    print ("Paused for 5.5 seconds for config t command")
    for n in range (901,940):
        print("Adding Vlan " + str(n) + "\n")
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" + str(n) + "\n")
        print("Finished removing Vlan " + str(n) + "\n")
    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()




