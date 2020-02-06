def men_from_boys(arr):
    odd = []
    even = []
    for item in arr:
        if item % 2 == 0:
            if item not in even:
              even.append(item)
        else:
            if item not in odd:
                odd.append(item)
    
    return sorted(even) + sorted(odd)[::-1]

# refactorized

def men_from_boys(arr):
    return sorted(item for item in set(arr) if item % 2 == 0) + sorted(item for item in set(arr) if item % 2 != 0)[::-1]