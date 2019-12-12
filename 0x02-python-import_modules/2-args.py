#!/usr/bin/python3


def arg(argv):
    add = len(argv) - 1

    if add == 0:
        print("{} arguments.".format(add))
    elif add == 1:
        print("{} argument:".format(add))
    else:
        print("{} arguments:".format(add))

    for i in range(1, add + 1):
        print("{:d}: {:s}".format(i, argv[i]))

if __name__ == '__main__':
    import sys
    arg(sys.argv)
