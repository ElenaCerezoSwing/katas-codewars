def pillars(num_pill, dist, width):
  # first we check if it is 1, the result is = because there is no anothe point to measure a distance to ;)
    if num_pill == 1:
        return 0
    # for other cases we have to calculate n-1(number of the distances) distances and add them to n-2 pillars' width (because we don't count the first and the last)
    else:
        return (num_pill - 1)*(dist * 100) + (num_pill - 2)*(width)