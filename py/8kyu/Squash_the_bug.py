def find_longest(string):
  # first we get the list of different string
    spl = string.split()
    #  we create an empty list
    longest = []
    for i in spl:
      # we push the string lengt of each item
        longest.append(len(i))
    # we return the max value
    return max(longest)