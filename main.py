#!/usr/bin/env python3

import sys
import time
from help_function import *

exec_time =int( input("How long do you want to run this (in min) ?") );
period = int( input("how many period do you want?") );

time_in_second = 60 * exec_time
step = convert_period(time_in_second)
_time_ = 0
count = 0
rand_list = []
while time_in_second > count:
    start = time.time()
    requests = int(get_req(_time_))
    print("At {:.1f}, generate {req} reequests".format(_time_, req = requests))
    for req in range (0,requests):
        rand_list.append(generate_rand())
    print(len(rand_list))
    _time_ += step     
    stop = time.time()
    print("time: ", stop-start)
    time.sleep(1-stop+start)
    count += 1   
    
