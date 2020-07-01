# Expected Time Complexity : O(N1/2)
# Expected Auxilliary Space :  O(1)

import math


def isPrime(N):
    # Your code here
    if N == 1:
        return True
    for i in range(2, 1 + int(math.sqrt(N))):
        if N % i == 0:
            return False
    return True


num = 15
print(isPrime(num))
