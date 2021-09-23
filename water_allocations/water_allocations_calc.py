"""
Created by: Noah Beebe and Penny Harding
Class: CSC365 Scripting Languages
Date: 9/21/2021
Water Allocations Calculator: use this program to figure out the number of days your tank will take to be depleted
"""

# Displays the opening header and subheader for the calculator
print()
print(f'Irrigation Water Allocation Calculator')
print(f'=' * 84)
print(f'This calculator determines how long it will take to use up an allocation of water.')
print()

# to keep the while loop going copied from the books program
choice = "y"
while choice.lower() == "y":

    # lets the user know what to enter to get it going
    while True:
        rationed_allocation = int(input('Rationed allocation depth in inches (D) : '))
        # tells the user to basically enter an amount that is not a negative or 0   depth
        if 0 < rationed_allocation:
            break
        else:
            # used to notify the user that the number they entered is bogus
            print('Invalid Value. Try again. ')

    # Lets user know what next prompt is
    while True:
        area_irrigated = int(input('Area being irrigated in acres (D) : '))
        # tells the user to basically enter an amount that is not a negative or 0
        if 0 < area_irrigated:
            break
        else:
            # used to notify the user that the number they entered is bogus
            print('Invalid Value. Try again. ')

    # Notifies user what to enter next
    while True:
        average_flow_rate = int(input('Average rate of flow in U.S. gallons per minute (D) : '))
        # tells the user to basically enter an amount that is not a negative or 0    gallons per minute
        if 0 < average_flow_rate:
            break
        else:
            # used to notify the user that the number they entered is bogus
            print('Invalid Value. Try again. ')

    # calculation goes here
    print()
    # rounds the multiply input from user to get the final result
    days_till_depleted = round((18.857 * rationed_allocation * area_irrigated) / average_flow_rate, 1)
    print("A " + str(rationed_allocation) + " inch allocation of water would be used up after "
          + str(days_till_depleted) + " days. ")

    # see if the user wants to continue
    print()
    choice = input('Continue (y/n)? ')
    print()

# lets the user know program has ended
print('Bye!')
