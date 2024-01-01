#!/usr/bin/env python

import subprocess
interface = input("enter the interface : ")
new_mac = input("enter the changing mac address : ")

print("[+] changing mac address for  "+interface+" to " + new_mac)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
