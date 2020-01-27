# It 's better with RegExp

def replace_exclamation(s):
   # We convert our string into a list
    s_list = list(s)
    for letter in s_list:
      # we convert each item of our list (if it is a vowel) into an exclamation mark
        if letter in 'aeiouAEIOU':
            s_list[s_list.index(letter)] = '!'
    # Finally we return the list converted into a string
    return "".join(s_list)

# Another working solution easier than previous one
def replace_exclamation(s):
  # We just check if letter is vowel and if it is, we replace it for an exclamation mark
    for letter in s:
        if letter in 'aeiouAEIOU':
            s = s.replace(letter,'!')
    return s