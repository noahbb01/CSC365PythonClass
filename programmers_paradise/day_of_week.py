# !/usr/bin/env python3

"""
This day of week def and module are all completed as well is added validation to ensure the
user types in a valid number 1-7
This code just asks the user to enter 1-7 on which day of the week starting with Sunday on which day they are
going to be checking into their room.

"""

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'Completed'

import validation

LINE_LENGTH = 55


def day_of_week():
    """
    I found this little bit of code on the internet that i found to fit my needs quite nicely.
    :return:
    """

    # Sets the weekday object and then displays the day of week based off of the number the user entered
    weekday = validation.get_range('Which day of the week will you be checking in? (Sunday = 1 and Saturday = 7) : ',
                                   low=1, high=7)
    if weekday == 1:
        print('\nSUNDAY Available Rooms')
    elif weekday == 2:
        print('\nMONDAY Available Rooms')
    elif weekday == 3:
        print('\nTUESDAY Available Rooms')
    elif weekday == 4:
        print('\nWEDNESDAY Available Rooms')
    elif weekday == 5:
        print('\nTHURSDAY Available Rooms')
    elif weekday == 6:
        print('\nFRIDAY Available Rooms')
    elif weekday == 7:
        print('\nSATURDAY Available Rooms')
    else:
        print('\nPlease enter any weekday number (1-7)')

    # Prompts the user back to the main menu screen
    print("=" * LINE_LENGTH)
    input('Press any key to continue... ')
    print("=" * LINE_LENGTH)


# Can call main to see if it would run without actually running it
if __name__ == '__main__':
    day_of_week()
