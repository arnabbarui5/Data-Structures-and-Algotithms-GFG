def natSum(N):
    if N == 0:
        return 0
    else:
        return N + natSum(N - 1)


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print("The Sum of Natural Number is ", natSum(num))
