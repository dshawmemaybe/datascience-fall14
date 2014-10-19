#!/bin/bash

cat worldcup.txt | sed 's/^! Team.*//; s/^.*fb|\([A-Z]\{3\}\).*/\1/' | 
    awk '/^\|-/ {print info; info = $0}
        !/^\|-/ {info = info", "$0;}
        END {print info}' | sed 's/^|-, //;' |
    awk -F', \\|' '/^.*$/ {
              print $1", "$2", "$3", "$4", "$5;
              }'