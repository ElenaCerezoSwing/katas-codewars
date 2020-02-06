def func_or(a,b):
    exclusion = ['', 0, [], {}, None, False]
    return (a or b not in exclusion)
    

def func_xor(a,b):
    exclusion = ['', 0, [], {}, None, False]
    return (a not in exclusion and b in exclusion) or (a in exclusion and b not in exclusion)
    