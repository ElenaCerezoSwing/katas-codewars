
def no_odds(values): 
   odd = []
    for value in values:
        if value == 0 or value % 2 == 0:
            odd.append(value)
    return odd

# refactorized solution 

def no_odds(values): 
    return [ value for value in values if value == 0 or value % 2 == 0]
