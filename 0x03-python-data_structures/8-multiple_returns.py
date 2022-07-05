#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == " ":
        return tuple(0, None)
    else:
        return tuple((len(sentence), sentence[0]))
