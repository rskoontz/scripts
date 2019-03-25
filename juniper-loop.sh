#!/bin/bash

for x in $(erg -e '%corpnet-stl4:ACCSW'); do echo -n "${x}: "; ssh $x "show system license keys"; done
