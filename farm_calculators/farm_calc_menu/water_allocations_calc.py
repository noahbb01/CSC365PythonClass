# !/usr/bin/env python3

"""
Created by: Noah Beebe and Penny Harding
Class: CSC365 Scripting Languages
Date: 9/21/2021
Water Allocations Calculator: use this program to figure out the number of days your tank will take to be depleted
"""


def water_allocations_calc():
    print(f'Irrigation Water Allocation Calculator')
    print(f'This calculator determines how long it will take to use up an allocation of water.')
    print('-' * 50)
    print()

    choice = "y"
    while choice.lower() == "y":

        while True:
            rationed_allocation = int(input('Rationed allocation depth in inches (D):\t'))
            # tells the user to basically enter an amount that is not a negative or 0   depth
            if 0 < rationed_allocation:
                break
            else:
                # used to notify the user that the number they entered is bogus
                print('Value must be above 0.')

        while True:
            area_irrigated = int(input('Area being irrigated in acres (A):\t\t\t'))
            # tells the user to basically enter an amount that is not a negative or 0
            if 0 < area_irrigated:
                break
            else:
                # used to notify the user that the number they entered is bogus
                print('Value must be above 0.')

        while True:
            average_flow_rate = int(input('Average rate of flow in US gpm (Q):\t\t\t'))
            # tells the user to basically enter an amount that is not a negative or 0    gallons per minute
            if 0 < average_flow_rate:
                break
            else:
                # used to notify the user that the number they entered is bogus
                print('Value must be above 0.')

        # calculation goes here
        days_till_depleted = round((18.857 * rationed_allocation * area_irrigated) / average_flow_rate, 1)
        print("A " + str(rationed_allocation) + " inch allocation of water would be used up after " + str(days_till_depleted) +
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
