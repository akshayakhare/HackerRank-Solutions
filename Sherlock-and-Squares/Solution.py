#!/bin/python

import math
import sys


t = int(raw_input().strip())
height = 1
for a0 in xrange(t):
    n = raw_input()
    x,y =n.split()
    i = int(math.sqrt(float(x)))
    j = int(math.sqrt(float(y)))
    count = 0
    for k in xrange(i,j+1):
        if int(x) <= int((math.pow(k,2))) <= int(y):
            count = count + 1
    print count
