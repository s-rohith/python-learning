#!/bin/bash

rm -rf output.csv output.json > /dev/null

df -h | sed -e "s/Mounted/Mounted_on/g" | awk '{$7=""; print $0}' | tr -s ' ' ',' | rev | cut -c2- | rev > output.csv