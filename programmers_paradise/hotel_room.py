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


def hotel_room():
    single = random.randint(0, 8)
    double = random.randint(0, 10)
    king = random.randint(0, 2)

    print(str(single) + ' single rooms (2 guest max) available at $96')
    print(str(double) + ' double rooms (4 guest max) available at $146')
    print(str(king) + ' king   rooms (2 guest max) available at $116')

    # add validation for correct room selection
    print()
    print('What type of room do you want to book?')
    room = int(input('1=Single, 2=Double, 3=King: '))
    print()

    # add validation for guest max
    guests = str(input('How many guests will be staying in the ' + str(room) + ' room? '))

    surcharge = 0
    if guests == 1:
        surcharge = 0
    elif guests == 2:
        surcharge = 10
    elif guests == 3:
        surcharge = 18
    elif guests == 4:
        surcharge = 32

    total = surcharge + room
    print(str('There is a $' + str(surcharge) + ' surcharge for ' + str(guests) + ' guests.'))
    print()

    nights = input('How many nights do you want to book a ' + str(room) + ' room ')
    print('with ' + str(guests) + ' guests, at ' + str(total) + ' a night? ')

    print('Please confirm booking for ' + str(nights) + ' nights total = ' + str(total) * int(nights))


# Can call main to see if it would run without actually running it
if __name__ == '__main__':
    hotel_room()
