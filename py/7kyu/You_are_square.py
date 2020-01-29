import math
def is_square(n): 
  # ternary operator for negative and positive numbers
  # check if sqrt is integer or not. With isinstance does not work properly
    return False  if n < 0 else math.sqrt(n) % 1 == 0