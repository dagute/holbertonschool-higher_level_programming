#!/usr/bin/python3
for x in range(89):
    if x / 10 < x % 10:
        print('{:02d}'.format(x), end=", ")
print('{:02d}'.format(x+1))
