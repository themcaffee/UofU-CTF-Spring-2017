#!/bin/bash

gcc -fno-stack-protector -m32 -D_FORTIFY_SOURCE=0 -o overflow main.c
