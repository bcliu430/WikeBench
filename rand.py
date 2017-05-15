## tested. This funtion can generate a 8060 mu, which is close to our coef
## this function is based on wikipedia trace file 
## the function is f(x) = (1/mu) * exp(1/mu)

import random

def generate_rand(mu = 8021.31):
    ran = random.expovariate(1/mu)
    return ran



def test():
    for i in range(0,50000):
       rand = generate_rand()
       with open("test","a+") as of:
           of.write(str(rand)+'\n')  


# test()
