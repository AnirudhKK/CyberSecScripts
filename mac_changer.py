#!/usr/bin/env python3

import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name to change MAC Address for")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address you want")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use -h or --help for more info.")
    elif not options.new_mac_address:
        parser.error("[-] Please specify a new MAC address you want, use -h or --help for more info.")
    return options

def change_mac(interface, new_mac_address):
    print("[+] Changing MAC address for "+interface+" to "+new_mac_address)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac_address])
    subprocess.call(["ifconfig",interface,"up"])

options = get_argument()
change_mac(options.interface, options.new_mac_address)