#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calculator(argv):
    adds = len(argv)
    if adds != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    if adds == 4:
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

if __name__ == '__main__':
    import sys
    calculator(sys.argv)
