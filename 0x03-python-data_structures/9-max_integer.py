#!/usr/bin/python3
def max_integer(my_list=[]):
    highest = my_list[0]
    if my_list == []:
        highest = None
    else:
        for num in my_list:
            if num > highest:
                highest = num
            else:
                highest = highest
        return highest
