# !/usr/bin/env python3

"""
Created by: Noah Beebe and Penny Harding
Class: CSC365 Scripting Languages
Date: 9/21/2021
Water Allocations Calculator: use this program to figure out the number of days your tank will take to be depleted

Updated: 10/6/2021
Added both positive number and number integrity code to module to ensure user is entering the correct information
"""

import validation

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__credits__ = ['Noah Beebe']
__version__ = '1.0.1'
__maintainer__ = 'Noah Beebe'
__email__ = 'nobeeb01@wsc.edu'
__status__ = 'Finished'


def water_allocations_calc():
    print(f'Irrigation Water Allocation Calculator')
    print(f'This calculator determines how long it will take to use up an allocation of water.')
    print('-' * 50)
    print()

    choice = "y"
    while choice.lower() == "y":

        # added validation to ensure user puts in a positive number
        while True:
            rationed_allocation = validation.get_positive_num('Rationed allocation depth in inches (D):\t')
            # tells the user to basically enter an amount that is not a negative or 0   depth
            if 0 < rationed_allocation:
                break
            else:
                # used to notify the user that the number they entered is bogus
                print('Value must be above 0.')

        # added validation to ensure user puts in a number
        while True:
            area_irrigated = validation.get_num('Area being irrigated in acres (A):\t\t\t')
            # tells the user to basically enter an amount that is not a negative or 0
            if 0 < area_irrigated:
                break
            else:
                # used to notify the user that the number they entered is bogus
                print('Value must be above 0.')

        # added validation to ensure user puts in a number
        while True:
            average_flow_rate = validation.get_num('Average rate of flow in US gpm (Q):\t\t\t')
            # tells the user to basically enter an amount that is not a negative or 0    gallons per minute
            if 0 < average_flow_rate:
                break
            else:
                # used to notify the user that the number they entered is bogus
                print('Value must be above 0.')

        # calculation goes here
        days_till_depleted = round((18.857 * rationed_allocation * area_irrigated) / average_flow_rate, 1)
        print("A " + str(rationed_allocation) + " inch allocation of water would be used up after " +
              str(days_till_depleted) +
              " days. ")

        # see if the user wants to continue
        print()
        choice = input('Continue (y/n)? ')
        print()

    # lets the user know program has ended
    print('Bye!')


# checks to see if this is running without actually running it
if __name__ == '__main__':
    water_allocations_calc()
