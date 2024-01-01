#!/usr/bin/env python
from subprocess import call

print("select no:1 for mac_changer")
print("select no:2 for network_scanner")
print("select no:3 for arp_spoofer")
print("select no:4 for packet_sniffer")
print("select no:5 for dns_spoofer")
choice = input("ENTER YOUR CHOICE OF TOOL YOU WANT USE : ")


class CallPy(object):

    def __init__(self, path="/root/PycharmProjects/pythonProject/arp_spoofer.py"):
        self.path = path

    def call_python_file(self):
        call(["python3", "{}".format(self.path)])


if choice == "1":
    c = CallPy()
    c.call_python_file()
