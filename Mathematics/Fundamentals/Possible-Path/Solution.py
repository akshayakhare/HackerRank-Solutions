import math
import sys
from fractions import gcd

t = int(input().strip())

for a0 in range(t):
    coord = input()
    px,py,qx,qy = (int(x) for x in coord.split())
    
    qnewx = qx - px
    qnewy = qy - py
    ## Since GCD of (px + d*py, py) is same as gcd of (px,py), and here 
    ## d can be -1 or 1, thus the the two coordinates are reachable if
    ## gcd of px,py is same as that of qx,qy
    gcd_origin = gcd(px,py)
    gcd_dest = gcd(qx,qy)
    
    possible = False
    if gcd_dest == gcd_origin:
        possible = True
    #possible = False
    #if qnewx%py == 0:
    #    if qnewy%px ==0:
    #        possible = True
    
    if possible:
        print("YES")
    else:
        print("NO")
