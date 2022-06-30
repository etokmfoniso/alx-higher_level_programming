if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    add = cal.add(a, b)
    sub = cal.sub(a, b)
    mul = cal.mul(a, b)
    div = cal.div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add))
    print("{:d} - {:d} = {:d}".format(a, b, sub))
    print("{:d} * {:d} = {:d}".format(a, b, mul))
    print("{:d} / {:d} = {:d}".format(a, b, div))
