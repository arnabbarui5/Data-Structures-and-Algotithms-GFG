def isPowerofTwo(n):
    ##Your code here
    if n!=0 and (n & (n-1))==0:
        return True
    else:
        return False