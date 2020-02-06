def max_number(n):
    lst = [int(i) for i in str(n)]
    return int(''.join(str(i) for i in sorted(lst)[::-1]))