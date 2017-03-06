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
dire = "./trace_files/"
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
            size = str(size)
            with open("size.out", "a+") as output:
                output.write(size+'\n')
    

def occurence():
    with open("size.out","r") as out:
        lines = out.readlines()
    for line in lines:
        sizelist.append(line)
    histo(sizelist,0,50000,20)    

def histo(mylist, low, high, bins):
    step = (high - low + 0.0)/bins
    dist = collections.Counter((float(i)-low)//step for i in mylist)
    dict_out = {}
    Sum = 0
    for b in range(bins):
        dist[b] = dist[b]/sum(dist)*100
        dict_out.update({2500*b : dist[b]})
    plot(dict_out)

def plot(mydict):
    print(mydict)
    plt.bar(range(len(mydict)), mydict.values(),align='center')
#    plt.xticks(range(len(mydict)), mydict.keys(),rotation=25)
    plt.xlabel('size of wikipedia web')
    plt.ylabel('percentage of occurance')
    plt.title('Wikipedia Tracefile')
    plt.savefig('percentage_plot_0.5s_3_trace.png')    


def main():
    getUrl()
    occurence()

main()

