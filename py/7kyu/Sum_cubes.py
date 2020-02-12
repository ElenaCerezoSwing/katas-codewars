def sum_cubes(n):
    nums = [item for item in range(1, n + 1, 1)] 
    return sum([item**3 for item in nums])


# refactorized:
def sum_cubes(n):
    return sum([item**3 for item in range(1, n + 1, 1)])