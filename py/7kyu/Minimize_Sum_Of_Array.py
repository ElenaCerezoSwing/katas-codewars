def min_sum(arr):
    result = 0
    for i in range(int((len(arr) / 2 ))) :
        result += sorted(arr)[i] * sorted(arr)[-(i + 1)]
    return result