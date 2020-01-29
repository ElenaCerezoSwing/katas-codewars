def tidyNumber(n):
        # convert integer to a list of integers
        lst = [int(i) for i in str(n)]
        # sort that list
        sorted_lst = sorted(lst)
        # convert list into an integer
        sorted_n = int(''.join(str(i) for i in sorted_lst))
        # check if sorted number is equal to input number
        return n == sorted_n