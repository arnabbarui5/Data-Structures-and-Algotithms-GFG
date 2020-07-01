def greyConverter(n):
    # Your code here
    bin_rep = bin(n)[2:]
    gray = bin_rep[0]
    for i in range(1,len(bin_rep)):
        gray += str(int(bin_rep[i-1]) ^ int(bin_rep[i]))
    return int(gray,2)