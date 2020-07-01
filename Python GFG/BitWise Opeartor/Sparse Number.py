def isSparse(n):
    #Your code here
    bin_rep = bin(n)[2:]
    k = bin_rep[0]
    for i in range(len(bin_rep[1:])):
        if k == '1':
            if bin_rep[1:][i] == k:
                return False
            else:
                k = bin_rep[1:][i]
        else:
            k = bin_rep[1:][i]
    return True