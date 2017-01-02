import math

t = int(input())

for a0 in range(t):
    Number = int(input())
    count = 0
    if Number%2 == 0:
        
        ## Started with count + 1 since the original number will also be divisible
        ## by 2, and we are not going to consider that in the loop
        count = count + 1
        
        ## Going till square root numbers will be enough
        for i in range(2,int(math.sqrt(Number))+1):
            ## First condition to check if it is divisible by the index and also the 
            ## index is divisible by 2
            if Number % i == 0 and i % 2 ==0:
                count = count + 1
            
            ## The second condition checks 3 conditions and in short, we find out if 
            ## the prime factors on division give us another factor of 2.
            if Number % (Number / i) == 0 and Number / i != i and Number/i % 2 == 0:
                count = count + 1
        
    print(count)
