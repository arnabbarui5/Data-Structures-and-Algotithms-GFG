def countSetBits(n):
    ##Your code here
    S = 0
    for i in range(1,n+1):
        bin_rep = bin(i)[2:]
        S += bin_rep.count('1')
    return (S)