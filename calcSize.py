#!/usr/bin/env python
import urllib2
import sys
import collections
import matplotlib.pyplot as plt
import json
import os

urls = []
sizelist = []
sortdict = {}
dire = "./trace/"
Files = os.listdir(dire)

def getUrl():
 #   f = open('stats','w')
    global urls
    for inf in Files: 
        with open(dire+inf) as f:
            lines = f.readlines()
        for line in lines:
            urls.append( line.split(' ')[2])
    calcSize(urls)

def calcSize(urls):
    global sortdict
    valid_url = 0
    urlLessThan50k = 0
#    fout = open('stats','w')
    length = len(urls)/7200  # 1hour /7200 = 0.5sec
    for i in range(length):
        try:
            U = urllib2.urlopen(urls[i])
            valid_url += 1
        except:
            continue
        size = len(U.read())
        if( size <= 50000):
            urlLessThan50k += 1 
            sizelist.append(size)
    fout = open('stats','w')
    out = "urls: " + str(length) + " valid: " + str(valid_url) + " url < 50k: " + str(urlLessThan50k)
    fout.write(out)
    fout.close()     
    plt.hist(sizelist,bins=20)
    plt.xlabel('size of wikipedia')
    plt.ylabel('occurance')
    plt.title('Wikipedia Tracefile')
    plt.savefig('plot.png')    

def main():
    getUrl()

main()

