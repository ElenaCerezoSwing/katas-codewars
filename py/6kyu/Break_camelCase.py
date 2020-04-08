def solution(s):
    new_s = []
    for letter in s:
        if letter.islower() == True:
            new_s.append(letter)
        else:
            letter = ' ' + letter
            new_s.append(letter)
    return ''.join(new_s)
    