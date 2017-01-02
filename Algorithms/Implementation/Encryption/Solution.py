## https://www.hackerrank.com/challenges/encryption

#!/bin/python3
import math
import sys


s = input().strip()

L = len(s)
rows = math.floor(math.sqrt(L))
cols = math.ceil(math.sqrt(L))

## Adds another row if the product is less than 
## the actual length
if (rows*cols < L):
    rows = rows + 1
    
## splits into a list of strings of length "cols"
enc_arr = [s[i:i+cols]for i in range(0, L, cols)]

## If the last element is not the same size, adjust
if(len(enc_arr[-1])<cols):
    enc_arr[-1]=enc_arr[-1]+' '*(cols - len(enc_arr[-1]))
#print(enc_arr[-1],"ah?")
dec_arr = []

## Loop adjacently to get the desired output
i = 0
while(i<cols):
    str = ""
    for j in range(0,rows):
        str += enc_arr[j][i]
    ## Added strip to handle the last string with added spaces
    dec_arr.append(str.strip())
    i = i + 1
final_cal = " ".join(dec_arr)
print(final_cal)
