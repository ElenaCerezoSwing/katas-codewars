def digitize(n):
    number_to_str = str(n)
    str_to_list =list(number_to_str)
    int_list = list(map(lambda x: int(x),str_to_list))
    return int_list[::-1]