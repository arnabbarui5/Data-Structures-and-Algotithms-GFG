# ------------------METHOD 1--------------------------

# count = 0
#
#
# def fun(N):
#     global count
#     if N > 0:
#         count = count + 1
#         return fun(N // 10)
#     return count


# ------------------------METHOD 2-------------------------

def fun(N):
    return len(str(N))


if __name__ == "__main__":
    num = int(input("Enter Number : "))
    print(fun(num))
