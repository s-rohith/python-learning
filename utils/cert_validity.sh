#!/bin/bash

rm -rf ./output/output.csv > /dev/null

cert_path="/etc/ssl/certs/CA_Disig_Root_R2.pem"

n=$(openssl x509 -noout -dates -in "${cert_path}" | wc -l)

for((i=1;i<=n;++i)); do
    m=$(openssl x509 -noout -dates -in "${cert_path}"  | cut -d '=' -f "$i" | tr "\n" "," | rev | cut -c2- | rev ) 
    echo $m >> ./output/output.csv
    # out+=$m
done

# echo $out
# cat c_test.csv | rev | cut -c2- | rev |  jq -nR '[ 
#     ( input | split(",") ) as $keys | 
#     ( inputs | split(",") ) as $vals | 
#     [ [$keys, $vals] | 
#     transpose[] | 
#     {key:.[0],value:.[1]} ] | 
#     from_entries ]' > output.json

# cat output.json


