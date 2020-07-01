def checkKthBit(n, k):
    # Your code here
    if n & (1 << k) != 0:
        return True
    else:
        return False
