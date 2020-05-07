#!/bin/bash

read -e -p "Enter Target: "  target
git clone https://github.com/j3ssie/Osmedeus
cd Osmedeus
./install.sh
wget -O/etc/chromium-browser/default https://raw.githubusercontent.com/mhmh55516/mexmos/master/chromium-flags
./osmedeus.py -t $target
