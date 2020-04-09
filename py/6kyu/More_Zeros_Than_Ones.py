def more_zeros(s):
    condition = []
    # First of all we convert into a binary from string
    binary_list = [format(i, 'b') for i in bytearray(s, encoding='utf-8')]
    for item in binary_list:
        # we count the occurrencies of each value
        ones = item.count('1')
        zeros = item.count('0')
        # chr(int(item, 2) is the ASCII value of out binary integer
        # If it is not in our array, we push it to it
        if zeros > ones and chr(int(item, 2)) not in condition:
          condition.append(chr(int(item, 2)))
    return condition