# !/usr/bin/env python3

"""
Main page to display the start of the calculator. My program was being buggy like it would not like half the code i
typed out and it kept running the same code even though i commented all instances of it out.

i debug the program and it says my hotel room is callable but i did not change anything

update: i got to run my hotel room. i just had to restart pycharm bc it was being dumb

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
    hotel_rooms()


if __name__ == '__main__':
    main()
