#!/usr/bin/env bash

# Build the solution for binary tweak

cd lib_solution
gcc -shared -fPIC -o libtweak.so tweaksolution.c
cd ../
gcc main.c -o binary_tweak -L./lib_solution -ltweak
export LD_LIBRARY_PATH_BACKUP=$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./lib_solution
