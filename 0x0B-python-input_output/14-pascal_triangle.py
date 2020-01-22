#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    my_list = []
    if n <= 0:
        return my_list

    row = [1]
    k = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [l + r for l, r in zip(row + k, k + row)]
    return my_list
