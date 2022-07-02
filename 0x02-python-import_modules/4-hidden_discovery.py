#!/usr/bin/python3
import hidden_4 as h
var = dir(h)
for i in range(var):
    if i != "__":
        print(var[i])
