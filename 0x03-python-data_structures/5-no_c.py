#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string
    del_string = "Cc"
    for char in del_string:
        new_string = new_string.replace(char, "")
    return new_string
