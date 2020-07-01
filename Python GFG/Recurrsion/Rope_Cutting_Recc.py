def maxCuts(N, A, B, C):
    if N == 0:
        return 0
    if N < 0:
        return -1
    res = max(maxCuts(N - A, A, B, C),
              maxCuts(N - B, A, B, C),
              maxCuts(N - C, A, B, C))

    if res == -1:
        return -1
    return res + 1


if __name__ == "__main__":
    n = int(input("Enter the length of rope : "))
    a = int(input("Enter first cut : "))
    b = int(input("Enter second cut : "))
    c = int(input("Enter third cut : "))

    print("Maximum number of cuts Possible is :", maxCuts(n, a, b, c))
