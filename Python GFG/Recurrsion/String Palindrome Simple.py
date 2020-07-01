def pal(N):
    if N == N[::-1]:
        return True
    else:
        return False


Say = str(input("Enter a String : "))
print(pal(Say))

