# !/usr/bin/env python3

"""
This is docstring stuff

"""

import random

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'Coding'

LINE_LENGTH = 55
weekdays = input('What day of week were you going to be checking in again? ')


def surcharge():
    sur_price = 0

    print()
    print('What type of room do you want to book?')
    room_choice = input('s=Single, d=Double, k=King: ')
    print()

    # add validation for correct guest selection
    guests = input('How many people will be staying in the ' + room_choice + ' room? ')
    if guests == 1:
        sur_price = 0
    elif guests == 2:
        sur_price = 10
    elif guests == 3:
        sur_price = 18
    elif guests == 4:
        sur_price = 32
    else:
        print(sur_price)

    print('There is a $' + str(sur_price) + ' surcharge for ' + str(guests) + ' guests.')


def dow_charge():
    if weekdays == 1 or 2 or 3:
        costs = 96
        return costs
    elif weekdays == 4 or 5:
        costs = 88
        return costs
    else:
        print('$80')


def hotel_rooms(single_room=dow_charge(), double_room=dow_charge()*1.5, king_room=dow_charge()*1.25):
    single = random.randint(0, 8)
    double = random.randint(0, 10)
    king = random.randint(0, 2)

    # don't hard code price bc of day of week rate should be displayed there
    print(str(single) + ' single rooms (2 guest max) available at ' + str(single_room))
    print(str(double) + ' double rooms (4 guest max) available at ' + str(double_room))
    print(str(king) + ' king   rooms (2 guest max) available at ' + str(king_room))

    surcharge()
    print()

    nights = int(input('How many nights would you be staying? '))
    return nights


# Can call main to see if it would run without actually running it
if __name__ == '__main__':
    hotel_rooms()
