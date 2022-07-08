#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary == None:
        return None
    else:
        for value in a_dictionary.values():
            if value > max:
                max = value
            else:
                max = max
        for key in a_dictionary:
            if a_dictionary[key] == max:
                return key
