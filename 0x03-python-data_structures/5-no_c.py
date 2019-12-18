#!/usr/bin/env python3


def no_c(my_string):
    new_word = ''
    for word in range(len(my_string)):
        if my_string[word] != 'c' and my_string[word] != 'C':
            new_word += my_string[word]
    return new_word
