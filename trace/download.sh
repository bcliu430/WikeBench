#!/bin/bash

set -euo pipefail

(lynx --dump http://www.wikibench.eu/wiki/2007-09/ | awk '/http/{print$2}') > web_list

file="./web_list"

while IFS= read line; do 
    wget $line
done < $file

for file in $*; do
    gzip -d $file || true
done
