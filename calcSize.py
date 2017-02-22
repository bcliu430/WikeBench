#!/usr/bin/env python
import urllib2
import sys

urls = []
Sum = 0
def getUrl(inf):
    global urls
    with open(inf) as f:
         lines = f.readlines()

    for line in lines:
        urls.append( line.split(' ')[2])
    calcSize(urls)

def calcSize(urls):
    global Sum
    for url in urls:
        try:
            U = urllib2.urlopen(url)
        except:
            continue
    size = len(U.read())
    Sum+= size

def main():
    getUrl(sys.argv[1])


main()

print Sum, len(urls)
