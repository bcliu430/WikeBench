## tested. This funtion can generate a 8060 mu, which is close to our coef

import random

mu = 8021.31 # exponential function coef

def generate_rand():
    ran = random.expovariate(1/mu)
    return ran



def test():
    for i in range(0,50000):
       rand = generate_rand()
       with open("test","a+") as of:
           of.write(str(rand)+'\n')  


# test()
