#!/usr/bin/env python
import netfilterqueue
import scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    print(scapy_packet.show())


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()