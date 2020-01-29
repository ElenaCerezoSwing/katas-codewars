def create_phone_number(n):
    # we create a reusable function that returns a string from a list from a bigger list
    def get_string_numb(s, e):
        return ''.join(str(i) for i in n[s:e])
    return '({}) {}-{}'.format(get_string_numb(0,3), get_string_numb(3,6), get_string_numb(6, len(n)))
    
    