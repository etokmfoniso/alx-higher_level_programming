#!/usr/bin/python3
def islower(c):
    for letter in range(chr(97), chr(123)):
        if c == letter:
            return True
        else:
            return False
