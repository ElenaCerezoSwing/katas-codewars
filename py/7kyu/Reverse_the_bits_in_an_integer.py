def reverse_bits(n):
    binar = (bin(n).replace("0b", ""))[::-1]
    new = int(binar, 2)
    return new