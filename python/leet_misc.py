

def hammingWeight(n):
    """Number of 1 Bits

    Write a function that takes an unsigned integer and return the number of '1'
    bits it has (also known as the Hamming weight).
    """

    count = 0
    for i in range(32):
        count += (n >> i) & 1
    return count


