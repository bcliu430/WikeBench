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
    global urls
    for inf in Files: 
        with open(dire+inf) as f:
            lines = f.readlines()
        for line in lines:
            urls.append( line.split(' ')[2])
    saveSize(urls)

def saveSize(urls):
    global sortdict
    valid_url = 0
    urlLessThan50k = 0
    length = len(urls)/7200  # 1hour /7200 = 0.5sec
    for i in range(length):
        try:
            U = urllib2.urlopen(urls[i])
            valid_url += 1
        except:
            continue
        size = len(U.read())
        if( size <= 50000):
	    with open ("data.out","a") as output:
	    	output.write(size)
'''		
    
    plt.hist(sizelist,bins=20)
    plt.xlabel('size of wikipedia')
    plt.ylabel('occurance')
    plt.title('Wikipedia Tracefile')
    plt.savefig('plot.png')    
'''

def main():
    getUrl()

main()

