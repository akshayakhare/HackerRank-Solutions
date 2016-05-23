#!/bin/python

import sys


t = int(raw_input().strip())
height = 1
for a0 in xrange(t):
    n = int(raw_input().strip())
    for count in xrange(n+1):
        if count == 0:
            height = 1
        else:
            if count % 2 == 1:
                height = height * 2
            else:
                height = height + 1
    print height
