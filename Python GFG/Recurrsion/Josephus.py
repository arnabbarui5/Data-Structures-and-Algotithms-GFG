def josephus(N, K):
    if N == 1:
        return N
    else:
        return (josephus(N - 1, K) + K - 1) % N + 1


if __name__ == "__main__":
    n = int(input("Enter value of n : "))
    k = int(input("Enter value of k : "))

    print("result is : ", josephus(n, k))
