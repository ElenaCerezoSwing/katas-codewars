def get_grade(s1, s2, s3):
    s = (s1 + s2 +s3)/3
    result = ''
    if s >= 90:
        result = 'A'
    elif s >= 80:
        result = 'B'
    elif s >= 70:
        result = 'C'   
    elif s >= 60:
        result = 'D'  
    else:
        result = 'F'  
    return result
    