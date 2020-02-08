def spin_words(sentence):
    if ' ' not in sentence and len(sentence)> 4:
        return ''.join(sentence[::-1])
    else:
        acc = sentence.split(' ')
        for i in range(len(acc)):
            if len(acc[i]) > 4:
                acc[i] = acc[i][::-1]
        return ' '.join(acc)