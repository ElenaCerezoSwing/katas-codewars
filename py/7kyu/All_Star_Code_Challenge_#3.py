def remove_vowels(strng):
    acc = []
    for i in strng:
        if i not in "aeiou":
            acc.append(i)
    return ''.join(acc)

# refactorized:

def remove_vowels(strng):
    return ''.join([i for i in strng if i not in "aeiou"])