#!/usr/bin/python3
import hidden_4


def names():
    for x in dir(hidden_4):
        if x[0] != '_':
            print(x)

if __name__ == '__main__':
    names()
