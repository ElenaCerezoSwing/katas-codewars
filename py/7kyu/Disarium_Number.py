def number_to_list(x): 
    return list(map(int, str(x)))

def disarium_number(number):
    listed_number = number_to_list(number)
    if sum([pow(listed_number[index], (index + 1)) for index in range(len(listed_number))]) == number:
        return "Disarium !!"
    else:
        return "Not !!"