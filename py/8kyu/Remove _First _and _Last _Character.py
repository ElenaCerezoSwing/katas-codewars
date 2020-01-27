def remove_char(s):
  # We convert the string into a list
    a = list(s)
    # We remove the first item
    a.pop(0)
    # Then, we remove the last item
    a.pop(-1)
    # The reuslt is the list joined into a string
    return "".join(a)