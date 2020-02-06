def absent_vowel(x): 
    vow = ['a', 'e', 'i', 'o', 'u']
    res = []
    for vowel in vow:
        if vowel not in x:
            res.append(vowel)
    return vow.index(res[0])