#!/usr/bin/python3
def islower(c):
    for letter in range(ord('a'), ord('z') + 1):
        if c == letter:
            return True
        else:
            return False
