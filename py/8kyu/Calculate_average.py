def find_average(array):
  # We will return the sum of the items of our given array dividied by its length in case the array != []
    return [sum(array)/len(array), 0][array == []]