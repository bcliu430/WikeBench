import random
from math import *
'''
 this function is generate a number of requests based on the wikipedia trace file
 the function we got is f(x) = a0+a1*cos(t*w)+b1*sin(t*w)
 where in this case 
 a0 = 2.845*pow(10,5)
 a1 = 6.817*pow(10,4)
 b1 = -4.6*pow(10,4)
 w = 0.2628 
'''

def get_req(xx,
            a0 = 2.845*pow(10,5),\
             a1 = 6.817*pow(10,4),\
             b1 = -4.6*pow(10,4),\
             w = 0.2628):
    requests = a0+a1*cos(xx*w)+b1*sin(xx*w)
    return requests


def generate_rand(mu = 8021.31):
    ran = random.expovariate(1/mu)
    return ran



def convert_period(time_in_sec):
    return 24/time_in_sec
