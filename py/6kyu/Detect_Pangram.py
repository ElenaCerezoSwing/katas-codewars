import string

def is_pangram(s):
    alpha = ''.join(set([i.lower() for i in s if i.isalpha()]))
    return len(alpha) == 26