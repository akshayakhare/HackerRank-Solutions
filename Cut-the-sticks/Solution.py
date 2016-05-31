import sys

n = int(raw_input().strip())
arr = []
arr = map(int,raw_input().strip().split(' '))
#print len(arr)
while len(arr)!=0:
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    print len(arr)
    while arr.__contains__(min):
        arr.remove(min)
    #print len(arr),arr
