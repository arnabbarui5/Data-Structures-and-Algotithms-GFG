def rec1toN(N):
    if N == 0:
        return
    else:
        rec1toN(N - 1)
        print(N, end=' ')


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print(rec1toN(num))
