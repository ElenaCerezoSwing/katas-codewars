def find_all(array, n):
    res = []
    for i in range(len(array)):
        if n == array[i]:
            res.append(i)
    return res

# refactorized
def find_all(array, n):
    return [i for i in range(len(array)) if n == array[i]]