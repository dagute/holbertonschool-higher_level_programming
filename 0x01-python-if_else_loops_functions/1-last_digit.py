#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number <= 0:
    lastdigit = number % -10
elif number >= 0:
    lastdigit = number % 10
if number % 10 > 5:
    print('Last digit of', number, 'is', lastdigit, 'and is greater than 5')
elif number % 10 == 0:
    print('Last digit of', number, 'is', lastdigit, 'and is 0')
else:
    print('Last digit of', number, 'is', lastdigit, 'and is less than 6 and not 0')
