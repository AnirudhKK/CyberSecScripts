#!/usr/bin/env python3

import argparse
import requests

def get_argument():
    parser=argparse.ArgumentParser()	
    parser.add_argument("-u","--url",dest="url",help="URL to download from")
    options = parser.parse_args()
    return options

def download_from_link(url):
    filename = url.split("/")[-1]
    get_response = requests.get(url)
    with open(filename, "wb") as output_file:
        output_file.write(get_response.content)

options = get_argument()
download_from_link(options.url)
print("Download Complete!")