def fibo(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fibo(N - 1) + fibo(N - 2)


def fibo_series(nterms):
    n1, n2 = 0, 1
    count = 0
    print("Fibonacci Series is :")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print("The Program Executed with T(n) = O(N)")


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print("The fibonacci number is ", fibo(num))
    print(fibo_series(num))
