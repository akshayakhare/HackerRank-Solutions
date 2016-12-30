## https://www.hackerrank.com/challenges/connecting-towns

import math
import sys

t = int(input().strip())
#print("t is",t)
for a0 in range(t):
    towns = int(input())
    #print("towns",towns)
    final_value = 1
    values =[]
    values = input().strip()
    nums = [int(n) for n in values.split()]
    #print("nums",nums)
    #print("values",values)
    for b0 in range(towns-1):
        final_value = final_value * nums[b0]
    final_value = final_value%1234567
    print(final_value)
