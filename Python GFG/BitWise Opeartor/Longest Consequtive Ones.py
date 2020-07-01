def maxConsecutiveOnes(x):
    ##Your code here
    bin_rep = bin(x)[2:]
    str1s = bin_rep.split('0')
    # if the problem is about longest consecutive zeros
    # then 1 is used as delimiter/separator
    # str0s = bin_rep.split('1')
    return max([len(u) for u in str1s])
