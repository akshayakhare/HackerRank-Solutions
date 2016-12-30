## https://www.hackerrank.com/challenges/sherlock-and-moving-tiles?h_r=next-challenge&h_v=zen

import math
import sys

values = input()
L,S1,S2 =  [int(n) for n in values.split()]
## Taking the relative speed, because nothing else matters
S = abs((S2 - S1))
#print(L,S1,S2,S)
t = int(input().strip())
#print("t is",t)
for a0 in range(t):
    area = int(input())
    
    ## The side would be square root of the area
    ## Then the side we want to reach would be 
    ## the Length - side calculated
    side = L - math.sqrt(area)
    
    ## diagonal because the velocity is in the diagonal side
    diagonal_side = math.sqrt(2*(side**2))
    #print(diagonal_side)
    ## Now its just basic maths, time = distance / speed
    time = diagonal_side / S
    print(time)
