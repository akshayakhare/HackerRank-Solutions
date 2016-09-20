#!/bin/python3

import sys

T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    total_handshakes = int(N*(N-1)/2)
    #while N > 0:
    #    N = N-1
    #    total_handshakes = total_handshakes + N
    print(total_handshakes)
