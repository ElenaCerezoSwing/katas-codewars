import collections

def duplicate_count(text):
    letters = list(text.lower())
    cuenta = collections.Counter(letters)
    repeated = 0
    for key in cuenta.keys():
        if cuenta[key] > 1:
            repeated += 1
    
    return repeated