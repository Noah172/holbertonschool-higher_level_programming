#!/usr/bin/python3
""" 
python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as i:
    print("Body response:")
    print("\t- type: {}".format(type(i.read(300))))
    print("\t- content: {}".format(i.read(300)))
    print("\t- utf8 content: {}".format(i.read(100).decode('utf-8')))
