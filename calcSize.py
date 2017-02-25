#!/usr/bin/env python
import urllib2
import sys
import collections
#import numpy as np
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

urls = []
sizelist = []
def getUrl(inf):
    global urls
    with open(inf) as f:
         lines = f.readlines()

    for line in lines:
        urls.append( line.split(' ')[2])
    calcSize(urls)

def calcSize(urls):
    global sortdict
    for url in urls:
        try:
            U = urllib2.urlopen(url)
        except:
            continue
        size = len(U.read())
        sizelist.append(size)
        sortdict = {x:sizelist.count(x) for x in sizelist}     

def plot():
    plt.bar( range(len(sortdict)), sortdict.values(), align='center')
    plt.xticks(range(len(sortdict)),sortdict.keys())
    plt.xlabel('size of wikipedia')
    plt.ylabel('occurance')
    plt.title('Wikipedia Tracefile')
    plt.grid(True)
    plt.savefig('result.pdf')    

def main():
    getUrl(sys.argv[1])
    plot()

main()
