def sum_str(a, b):
    if a == '' and b == '':
        return '0'
    elif b == '':
        return a
    elif a == '':
        return b
    else:    
        return str(int(a) + int(b)) 