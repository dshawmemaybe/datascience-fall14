#!/bin/bash

cat cmsc.txt | awk '/^CMSC[0-9]*$/ {class=$0}
    /^0/ {print rest; rest = class", "$0}
    !/^0|^CMSC[0-9]*$/ {rest = rest", "$0}' |
    sed 's/Seats (Total://; s/Open: //; s/Waitlist: \([0-9]*\))/\1/; s/\(M*Tu*W*Th*F*\)/\1,/; s/CSI\|ITV\|HBK\|AVW\|MTH\|JMP/\0,/; s/, $//'
