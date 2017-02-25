#!/usr/bin/env python
import urllib2
import sys
import collections
#import numpy as np
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import json

urls = []
sizelist = []
sortdict = {}
def getUrl(inf):
    global urls
    with open(inf) as f:
         lines = f.readlines()

    for line in lines:
        urls.append( line.split(' ')[2])
    calcSize(urls)

def calcSize(urls):
    global sortdict
    fout = open(sys.argv[1]+'.out','w')
    out = sys.argv[1] + '.pdf'
    length = len(urls)/3600  # 1hour /3600 = 1sec
    for i in range(length):
        try:
            U = urllib2.urlopen(urls[i])
        except:
            continue
        size = len(U.read())
        if( size <= 100000):
            sizelist.append(size)
    sortdict = {x:sizelist.count(x) for x in sizelist}
    print sortdict
    json.dump(sortdict,fout)    
    fout.close()     
    plt.hist(sizelist,bins=10)
    plt.xlabel('size of wikipedia')
    plt.ylabel('occurance')
    plt.title('Wikipedia Tracefile')
    plt.savefig(out)    

def main():
    getUrl(sys.argv[1])

main()

