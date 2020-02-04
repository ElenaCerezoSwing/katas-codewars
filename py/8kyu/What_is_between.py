def between(a,b):
    result = []
    for i in range(a, b +1, 1):
        result.append(i)
    return result
    

    # refactorized 
def between(a,b):
     return [i for i in range(a, b +1, 1)]