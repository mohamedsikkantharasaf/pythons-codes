import arp_spoofer
import packet_sniffer
import mac_changer2
import network_scanner
import dns_spoofer
import subprocess

#!/usr/bin/env python
import subprocess
print("PENETESTING SCRIPTING TOOL USING PYTHON\n----####----****----@@@@___---$$$$\n")
print("select no:1 for mac_changer")
print("select no:2 for network_scanner")
print("select no:3 for arp_spoofer")
print("select no:4 for packet_sniffer")
print("select no:5 for dns_spoofer")

choice = int(input("ENTER YOUR CHOICE OF TOOL YOU WANT USE = "))

if choice == 1:
    subprocess.call(["python3  mac_changer2.py"])
elif choice == 2:
    subprocess.call(["python3 network_scanner.py"])
elif choice == 3:
    subprocess.call(["python3  arp_spoofer.py"])
elif choice == 4:
    subprocess.call(["python3  packet_sniffer.py"])
elif choice == 5:
   subprocess.call(["python3  dns_spoofer.py"])

else:
    print('enter the correct choice')

class CallPy(object):

    def __init__(self, path="/root/PycharmProjects/pythonProject/arp_spoofer.py"):
        self.path = path

    def call_python_file(self):
        call(["python3", "{}".format(self.path)])





choice = input("ENTER YOUR CHOICE OF TOOL YOU WANT USE")

if __name__ == "__main__":
    c = CallPy()
    c.call_python_file()
