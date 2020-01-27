def problem(a):
  # First we check if it is not a string, it's important because it could be a float or an integer ;)
    if type(a) is not str:
      # result for this case
        return (a * 50) + 6
    else: 
      # result por values that are nor numbers
        return "Error"