#!/usr/bin/env python3

import scapy.all as scapy
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP(s)")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please enter IP!")
    return options.target

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc,"mac":element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(results_list):
    print("IP\t\t\tMAC ADDRESS\n-------------------------------------------------------")
    for client in results_list:
        print(client["ip"]+"\t\t"+client["mac"])

ip = get_argument()
scan_result = scan(ip)
print_result(scan_result)