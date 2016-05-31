import sys

n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
    i,j = raw_input().strip().split(' ')
    i,j = [int(i),int(j)]
    laneStart = i
    min = 4
    while laneStart <= j:
        if width[laneStart] < min:
            min = width[laneStart]
        laneStart = laneStart + 1
    if min > 3:
        min = 3
    print min
