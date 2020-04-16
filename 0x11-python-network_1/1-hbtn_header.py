#/usr/bin/python3
import urllib.request
from sys import argv

if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as i:
        pag = i.info()
        print(pag['X-Request-Id'])
