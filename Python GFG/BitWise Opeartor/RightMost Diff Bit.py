def posOfRightMostDiffBit(m,n):
    #Your code here
    if m==n:
        return -1
    else:
        num = ~(m^n)
        k = 1
        while True:
            if (num & (1<<(k-1)))==0:
                return k
            else:
                k += 1