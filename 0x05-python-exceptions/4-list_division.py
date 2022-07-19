#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_length = []
    try:
    for i, j in my_list_1, my_list_2:
        div = my_list_1[i] / my_list_2[j]
        list_length = list_length.append(div)
    except TypeError:
        div = 0
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
        div = 0
    except IndexError:
        print("out of range")
        div = 0
    finally:
        return (list_length)

