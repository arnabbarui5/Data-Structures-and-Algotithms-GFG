def getFirstSetBit(n):
    # Your code here
    bin_rep = bin(n)
    print(bin_rep)
    req_bin_rep = bin_rep[2:][::-1]
    print(req_bin_rep)
    if '1' not in req_bin_rep:
        return "0"
    else:
        for ind, val in enumerate(req_bin_rep):
            if val == '1':
                break
        return ind + 1


num = 12
print(getFirstSetBit(num))
