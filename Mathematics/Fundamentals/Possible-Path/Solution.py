import math
import sys

t = int(input().strip())

for a0 in range(t):
    coord = input()
    px,py,qx,qy = (int(x) for x in coord.split())
    
    qnewx = qx - px
    qnewy = qy - py
    
    possible = False
    if qnewx%py == 0:
        if qnewy%px ==0:
            possible = True
    
    if possible:
        print("YES")
    else:
        print("NO")
