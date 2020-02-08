def sum_of_minimums(numbers):
    acc = 0
    for i in numbers:
        i = sorted(i)
        acc += i[0]
    return acc
        