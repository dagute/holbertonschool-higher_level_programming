#!/usr/bin/python3


def infinite(argv):
    add = len(argv)
    suma = 0
    for x in range(1, add):
        suma += int(argv[x])
    print("{:d}".format(suma))

if __name__ == '__main__':
    import sys
    infinite(sys.argv)
