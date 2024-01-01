#!/usr/bin/env python
import netfilterqueue


def process_packet(packet):
    print(packet)
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(1, process_packet)
queue.run()