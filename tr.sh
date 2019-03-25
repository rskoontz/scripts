#!/bin/sh

OUTPUTFILE=~/Development/scripts/tr-output.txt
ping -c 1 8.8.8.8 >> $OUTPUTFILE
traceroute 8.8.4.4 >> $OUTPUTFILE
