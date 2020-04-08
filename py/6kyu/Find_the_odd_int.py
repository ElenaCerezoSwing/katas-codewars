def find_it(seq):
    tup = set(seq)
    freq = {}
    result = 0
    
    for number in tup:
        freq[number] = seq.count(number)
    for number, occur in freq.items():
        if occur%2 != 0:
            return number