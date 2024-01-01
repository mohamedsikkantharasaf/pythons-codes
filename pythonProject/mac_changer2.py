#!/usr/bin/env python

import subprocess
import optparse
import re


def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify the interface,use --help for more info.")
    if not options.new_mac:
        parser.error("[-] please specify the new_mac,use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w ", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read mac address.")


options = arguments()
current_mac = get_current_mac(options.interface)
print("current mac = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac != options.new_mac:
    print("[+] mac address was sucessfully changed to " + current_mac)
else:
    print("[-] mac address did not get changed")





