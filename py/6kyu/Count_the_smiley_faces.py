def count_smileys(arr):
    count = 0
    smiley = [':)', ':-)', ':~)',':D', ':-D', ':~D', ';)', ';-)', ';~)',';D', ';-D', ';~D']
    for item in arr:
       if item in smiley:
            count += 1
    return count