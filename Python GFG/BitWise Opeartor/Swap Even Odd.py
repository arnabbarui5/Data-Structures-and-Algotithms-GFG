def swapBits(n):
    #Your code here
    even_bits = n & 0xAAAAAAAA
    odd_bits = n & 0x55555555
    even_bits >>= 1
    odd_bits <<= 1
    return even_bits | odd_bits