def super_size(n):
    res = [int(i) for i in list(str(n))]
    return int("".join([str(i) for i in sorted(res)[::-1]]))