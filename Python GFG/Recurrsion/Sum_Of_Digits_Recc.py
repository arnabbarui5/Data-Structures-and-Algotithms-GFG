def sumOfDigits(N):
    if N < 10:
        return N
    else:
        return int(sumOfDigits(N / 10) + N % 10)


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print("The Sum Of Digits is ", sumOfDigits(num))
