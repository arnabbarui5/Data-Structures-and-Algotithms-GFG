def factorial(N):
    fact = 1

    if N == 1:
        return fact

    elif N == 0:
        return fact

    elif N > 1:
        for i in range(1, N + 1):
            fact = fact * i
        return fact
        print(fact)