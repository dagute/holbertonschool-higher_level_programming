#!/usr/bin/python3
def magic_string(str=[0]):
    str[0] += 1
    return (", ".join(["Holberton" for x in range(str[0])]))
