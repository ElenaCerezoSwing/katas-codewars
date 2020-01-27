def fake_bin(x):
  # First, we convert x into a list
    x_list = list(x)
    # We transform each item of our new list into its integer
    int_list = list(map(lambda x: int(x), x_list))
    # We create an empty list we will use later
    list_result = []
    # We go through our list with integers, if item >= 5, we add '1' to our storage list, if not, a "0"
    for item in int_list:
        if item >= 5:
            list_result.append("1")
        else: list_result.append("0")
    #Finally, we convert our final list into a string
    return "".join(list_result)