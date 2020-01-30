def lottery(s):
    import re
    # first we get our list
    s_lst = [i for i in s]
    # second we prepare an array with only digits
    acc = [ i  for i in s_lst  if i.isdigit()]
    acc2= []
    # third, we push only not repeated items
    for i in acc:
        if i not in acc2:
            acc2.append(i)
    # we give a result depending on if the string contains digits inside or not ;)
    return ''.join(acc2) if re.findall(r'[0-9]', str(s)) != [] else "One more run!"
    