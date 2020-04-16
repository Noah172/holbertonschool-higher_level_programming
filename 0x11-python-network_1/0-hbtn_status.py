#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as i:
        pag = i.read()
        print("Body response:")
        print("\t- type: {}".format(type(pag)))
        print("\t- content: {}".format(pag))
        print("\t- utf8 content: {}".format(pag.decode('utf-8')))
