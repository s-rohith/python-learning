#!/bin/bash
# Get output of df -h in json

rm -rf output.csv output.json > /dev/null

df -h | sed -e "s/Mounted/Mounted_on/g" | awk '{$7=""; print $0}' | 
    tr -s ' ' ',' | rev | cut -c2- | rev |  jq -nR '[ 
    ( input | split(",") ) as $keys | 
    ( inputs | split(",") ) as $vals | 
    [ [$keys, $vals] | 
    transpose[] | 
    {key:.[0],value:.[1]} ] | 
    from_entries ]' > output.json

cat output.json
