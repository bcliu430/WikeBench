#!/usr/bin/python

import os

WEB = os.system("lynx --dump http://www.wikibench.eu/wiki/2007-09/ | awk '/http/{print$2}'")

for web in WEB:
    os.system("wget web")


