def fact(N):
    if N == 0 or N == 1:
        return 1

    else:
        return N * fact(N - 1)


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print("The factorial of ", num, " is ", fact(num))
