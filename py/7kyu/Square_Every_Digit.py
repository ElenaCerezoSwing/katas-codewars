def square_digits(num):
    st = [int(i) for i in str(num)]
    return int(''.join([str(pow(i, 2)) for i in st]))
    