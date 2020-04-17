#!/usr/bin/python3
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        pag = response.headers.get("X-request-Id")
        print(pag)
