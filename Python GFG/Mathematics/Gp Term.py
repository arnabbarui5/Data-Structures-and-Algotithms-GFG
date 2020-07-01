import math


# Compelte his function
def termOfGP(A, B, N):
    # Your code here
    ratio = B / A
    return A * math.pow(ratio, N - 1)
