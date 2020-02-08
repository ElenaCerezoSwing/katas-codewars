def grabscrab(word, possible_words):
    res = []
    for wd in possible_words:
        if sorted(word) == sorted(wd):
            res.append(wd)
    return res

# refactorized:
def grabscrab(word, possible_words):
    return [wd for wd in possible_words if sorted(word) == sorted(wd)]