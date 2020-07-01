def grayToBinary(n):
    ##Your code here
    gray_rep = bin(n)[2:]
    binary = gray_rep[0]
    for i in range(1,len(gray_rep)):
        if gray_rep[i] == '0':
            binary += binary[i-1]
        else:
            binary += str(int(not int(binary[i-1])))
    return int(binary,2)