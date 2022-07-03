#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char == 'c' or char == 'C':
            new_string = my_string.replace(char, "")
            return new_string
        else:
            return my_string
