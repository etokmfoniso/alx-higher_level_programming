#!/usr/bin/python3
import hidden_4 as h
var = dir(h)
for list in var:
    if list[0] != "_":
        print(list)
__name__ == "__main__"
