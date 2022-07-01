#!/usr/bin/python3
from sys import argv


def system():
    summ = 0
    if len(argv) - 1 == 0:
        print("{:d}".format(summ))
    else:
        for i in range(1, len(argv)):
            summ += (int)(argv[i])
        print("{:d}".format(summ))


if __name__ == "__main__":
    system()
