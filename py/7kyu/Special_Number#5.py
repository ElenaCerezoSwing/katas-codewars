def special_number(number):
    import re
    return  "Special!!" if re.match('^[0-5]*$', str(number)) else "NOT!!"