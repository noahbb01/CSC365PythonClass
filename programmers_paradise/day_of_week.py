# !/usr/bin/env python3

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'Documentation'

LINE_LENGTH = 55


def day_of_week():
    """
    I found this little bit of code on the internet that i found to fit my needs quite nicely.
    :return:
    """
    while True:
        weekday = int(input('Which day of the week will you be checking in? (Monday = 1 and Sunday = 7) : '))
        if weekday == 1:
            print('\nMonday')
        elif weekday == 2:
            print('\nTuesday')
        elif weekday == 3:
            print('\nWednesday')
        elif weekday == 4:
            print('\nThursday')
        elif weekday == 5:
            print('\nFriday')
        elif weekday == 6:
            print('\nSaturday')
        elif weekday == 7:
            print('\nSunday')
        else:
            print('\nPlease enter any weekday number (1-7)')

        # Prompts the user back to the main menu screen
        print("=" * LINE_LENGTH)
        input('Press any key to continue... ')
        print("=" * LINE_LENGTH)


# Can call main to see if it would run without actually running it
if __name__ == '__main__':
    day_of_week()
