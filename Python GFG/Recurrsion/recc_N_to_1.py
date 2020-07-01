def fun(N):
    if N == 0:
        return
    else:
        print(N)
        fun(N - 1)


if __name__ == "__main__":
    num = int(input("Enter a nunber : "))
    print(fun(num))
