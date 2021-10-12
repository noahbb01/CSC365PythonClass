# !/usr/bin/env python3

"""
Blah Blah Blah

"""

from day_of_week import *
from hotel_room import *

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'In Progress'

# Global variable used for formatting in the code
LINE_LENGTH = 55


def menu_prompt():
    print('Python Programmer’s Paradise - Motel Booking System!')
    print('=' * LINE_LENGTH)


def main():
    menu_prompt()
    day_of_week()
    hotel_room()


if __name__ == '__main__':
    main()
