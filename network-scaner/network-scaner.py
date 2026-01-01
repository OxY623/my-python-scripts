#!/usr/bin/env python
import scapy.all as scapy



def scan(ip):
    # answered, unanswered = scapy.arping(ip, verbose=False)
    # return answered
    arp_request = scapy.ARP()
    print(arp_request.summary())

if __name__ == "__main__":
    result = scan("192.168.192.1/24")
    for sent, received in result:
        print(received.psrc, received.hwsrc)

