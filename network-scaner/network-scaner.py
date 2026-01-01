#!/usr/bin/env python3
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_request

    answered_list = scapy.srp(
        arp_req_broadcast,
        timeout=1,
        verbose=False
    )[0]

    clients_list = []

    for idx, el in enumerate(answered_list):
        client = {
            "id": idx,
            "ip": el[1].psrc,
            "mac": el[1].hwsrc
        }
        clients_list.append(client)

       

    return clients_list

def print_result(data):
    print("id\tIP\t\t\tMAC Address")
    print("---------------------------------------------------")
    for el in data:
        print(f"{el['id']}\t{el['ip']}\t\t{el['mac']}")
        print("---------------------------------------------------")


if __name__ == "__main__":
    result = scan("192.168.192.1/24")
    print_result(result)
