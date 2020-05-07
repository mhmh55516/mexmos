#!/bin/bash

read -s -p "Enter Target: "  target
git clone https://github.com/j3ssie/Osmedeus
cd Osmedeus
./install.sh
./osmedeus.py -t $target
