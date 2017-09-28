#!/usr/bin/env python
import getpass
import sys
import telnetlib
import time

HOST = "10.224.97.2"
password = getpass.getpass()
password2 = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("enable" + "\n")
tn.read_until("Password: ")
tn.write(password2 + "\n")
tn.write("conf t\n")
print ("Going into config t")
time.sleep(5.5) # pause 5.5 seconds
print ("pause over")
for n in range (901,941):
    tn.write("vlan " + str(n) + "\n")
    tn.write("name Python_VLAN_" + str(n) + "\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()


