## https://www.hackerrank.com/challenges/reverse-game

t = int(input().strip())

for a0 in range(t):
    values = input()
    N,K = [int(n) for n in values.split()]
    #print("N,k",N,K)
    pos = 1
    ## Now that we have the two values, after reversing at each position
    ## our final numbers would be something like below:
    ## 5 0 4 1 3 2
    ## 4 0 3 1 2
    ## This means bigger than half are in the odd places in reverse order
    ## Smaller than half would be in even places in correct order.
    ## After that, its simple logic to find out the correct position of each ball.
    ## As given below:
    if(K>=(N-1)/2):
        pos = (N-K)*2 - 2
    else:
        pos = (K+1)*2 - 1
        
    print(pos)
