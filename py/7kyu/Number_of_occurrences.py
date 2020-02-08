def number_of_occurrences(element, sample): 
   acc = 0
    for i in sample:
        if i == element:
            acc += 1
    return acc


# refactorized: 

def number_of_occurrences(element, sample):
    return len([i for i in sample if i == element])