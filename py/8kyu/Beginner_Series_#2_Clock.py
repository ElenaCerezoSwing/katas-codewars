def past(h, m, s):
    # We convert each item into seconds, we sum all of them and we multiply the sum by 1000 to obtain the result in ms
    return (h * 3600 + m * 60 + s) * 1000