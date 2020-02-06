def small_enough(array, limit):
    acc = []
    for item in array:
        if item > limit:
            acc.append(item)
    return len(acc) == 0