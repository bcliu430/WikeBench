#!/bin/bash

set -euo pipefail

# for file in ./trace_files/*; do
for file in ./test*; do
    echo $file
    ./calcSize.py $file
done
