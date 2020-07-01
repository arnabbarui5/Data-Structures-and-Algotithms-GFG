def digitalRoots(N):
    if N < 10:
        return N
    else:
        return digitalRoots(digitalRoots(N // 10) + N % 10)


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print(digitalRoots(num))
