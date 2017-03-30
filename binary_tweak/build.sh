#!/usr/bin/env bash

# Build the challenge files for binary_tweak

cd lib
gcc -shared -fPIC -o libtweak.so tweak.c
cd ../
gcc main.c -o binary_tweak -L./lib -ltweak
export LD_LIBRARY_PATH_BACK=$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./lib/
