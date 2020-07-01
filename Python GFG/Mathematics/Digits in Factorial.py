# Expected Time Complexity : O(N)
# Expected Auxilliary Space : O(1)

import math


def digitsInFactorial(N):
    # Your code here
    digits = 0

    if N <= 1:
        return N

    for i in range(2, N+1):
        digits += math.log10(i)

    return math.floor(digits) + 1


num = 5
print(digitsInFactorial(num))
