def sum_str(a, b):
    if a == '' and b == '':
        return '0'
    elif b == '':
        return a
    elif a == '':
        return b
    else:    
        return str(int(a) + int(b)) 

# refactorized :
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))