#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for n in range(x):
        try:
            print('{:d}'.format(my_list[n]), end="")
            number += 1
        except (ValueError, TypeError):
            n += 1
            continue
    print()
    return number
