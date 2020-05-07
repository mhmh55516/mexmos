#!/bin/bash

git clone https://github.com/j3ssie/Osmedeus
cd Osmedeus
./install.sh
read -p "Enter Target: "  target
./osmedeus.py -t $target
