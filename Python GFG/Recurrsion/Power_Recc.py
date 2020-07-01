def power(N, K):
    if K == 1:
        return N
    if K == 0:
        return 1
    else:
        return N * power(N, K-1)


if __name__ == "__main__":
    n = int(input("Enter number : "))
    p = int(input("power ? : "))

    print(power(n, p))
