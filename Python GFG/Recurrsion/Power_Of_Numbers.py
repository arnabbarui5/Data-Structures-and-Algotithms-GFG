def powerDigit(N, R):
    if R == 0:
        return 1

    return ((powerDigit(N, R - 1) % 1000000007) * N % 1000000007) % 1000000007

