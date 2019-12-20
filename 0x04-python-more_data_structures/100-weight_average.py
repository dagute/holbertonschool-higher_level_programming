#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    div = 0
    add = 0
    for x in my_list:
        add += x[0] * x[1]
        div += x[1]
    return add / div
