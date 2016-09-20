import math
import sys

t = int(input().strip())

for a0 in range(t):
    coord = input()
    # =coord.split()
    px,py,qx,qy = (int(x) for x in coord.split())
    
    dx = qx-px
    dy = qy-py

    sx = qx + dx
    sy = qy + dy

    print(sx , sy)
