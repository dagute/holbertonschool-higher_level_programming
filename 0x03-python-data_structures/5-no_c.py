#!/usr/bin/env python3


def no_c(my_string):
    new_word = ""
    for word in my_string:
        if word != 'c' and word != 'C':
            new_word += word
    return new_word
