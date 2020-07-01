def countBitsFlip(a,b):
    ##Your code here
    c = a ^ b
    cc = bin(c)[2:].count('1')
    return (cc)