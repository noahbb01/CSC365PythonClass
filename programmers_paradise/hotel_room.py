# !/usr/bin/env python3

"""
This is docstring stuff

"""

import random
from day_of_week import *

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'Coding'

LINE_LENGTH = 55


#def surcharge():
   # if guests == 1


def hotel_room():
    num1 = random.randint(0, 8)
    num2 = random.randint(0, 10)
    num3 = random.randint(0, 2)

    single = num1
    double = num2
    king = num3

    print(str(num1) + ' single rooms (2 guest max) available at $96')
    print(str(num2) + ' double rooms (4 guest max) available at $146')
    print(str(num3) + ' king   rooms (2 guest max) available at $116')

    # add validation for correct room selection
    print()
    print('What type of room do you want to book?')
    room = str(input('s=Single, d=Double, k=King: '))
    print()

    # add validation for guest max
    guests = str(input('How many guests will be staying in the ' + room + ' room? '))
    print(str('There is a ' + ))


# Can call main to see if it would run without actually running it
if __name__ == '__main__':
    hotel_room()
