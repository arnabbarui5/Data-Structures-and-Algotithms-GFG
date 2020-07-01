def exactly3Divisors(N):
    # Your code here
    count = 0
    i = 2
    while (i * i) <= N:
        flag = True
        j = 2
        while j <= i / 2:
            if i % j == 0:
                flag = False
            j += 1

        if flag:
            count += 1
        i += 1
    return count


num = 4
print(exactly3Divisors(num))
