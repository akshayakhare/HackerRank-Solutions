## https://www.hackerrank.com/challenges/summing-the-n-series?h_r=next-challenge&h_v=zen

import math
import sys

t = int(input().strip())
#print("test cases are: ",t)
for a0 in range(t):
    n = int(input())
    Sum = 0
    ## Apparently all the below code is irrelevant, and I'm stupid
    #for i in range(1,n+1):
    #    T = i*i - (i - 1)*(i - 1)
    #    Sum = Sum + T
    ## On solving the equation for sum, all the other terms gets 
    ## crossed off and only n^2 remains.
    Sum = n*n
    Sum = Sum%((10**9)+7)
    Sum = int(Sum)
    print(Sum)
