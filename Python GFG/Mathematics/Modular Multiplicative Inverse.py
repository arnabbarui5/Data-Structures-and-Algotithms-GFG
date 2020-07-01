def modInverse(a, m):
    # Your code here
    a = a % m

    for i in range(1, m):
        if ((a * i) % m) == 1:
            return i
    return -1
