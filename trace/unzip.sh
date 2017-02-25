#!/usr/bin/bash

for file in $*; do
    gzip -d $file
done
