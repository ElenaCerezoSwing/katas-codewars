def chromosome_check(sperm):
  # We just check if 'y' is in sperm. We use lower() to make sure all cases are included
    if 'y' in sperm.lower():
       return  'Congratulations! You\'re going to have a son.'
    else:
        return  'Congratulations! You\'re going to have a daughter.'

def chromosome_check(sperm):
  # This is the same but in one line
  return ['Congratulations! You\'re going to have a daughter.', 'Congratulations! You\'re going to have a son.']['y' in sperm.lower()]      