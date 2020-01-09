#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as err_msg:
        print("Exception: {}".format(err_msg), file=sys.stderr)
        return None
    return res
