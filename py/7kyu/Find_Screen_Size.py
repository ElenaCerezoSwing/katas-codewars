def find_screen_height(width, ratio): 
    width_factor = int(ratio.split(':')[0])
    height_factor = int(ratio.split(':')[1])
    return str(width) + 'x' + str(int(width * height_factor / width_factor))