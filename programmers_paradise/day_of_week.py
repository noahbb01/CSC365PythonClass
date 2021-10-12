# !/usr/bin/env python3

"""
This is docstring stuff

"""

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'Completed'

LINE_LENGTH = 55

"""
def room_rate():
    if int(weekday) in range(1, 3):
        dow_rate = 80 + (96 * 1.2)
        print(dow_rate)
    elif int(weekday) in range(4, 5):
        dow_rate = 80 + ()
    else:
        print('No')
"""


def day_of_week():
    """
    I found this little bit of code on the internet that i found to fit my needs quite nicely.
    :return:
    """

    weekday = int(input('Which day of the week will you be checking in? (Sunday = 1 and Saturday = 7) : '))
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

    def dow_charge():
        if weekday == 1 or 2 or 3:
            costs = 80 * 1.2
            print(costs)
        elif weekday == 4 or 5:
            costs = 80 * 1.1
            print(costs)
        else:
            print('$80')


# Can call main to see if it would run without actually running it
if __name__ == '__main__':
    day_of_week()
