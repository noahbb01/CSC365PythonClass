# !/usr/bin/env python3

"""
So what all this is supposed to do is get the day of week rate
display almost every numeric input value needed and calculate the final bill with pieces of info provided by cust

Finally got my surcharge function to work. had to had 'int' before input otherwise it kept display 0

other bugs: day of week function is buggy bc i don't think it works right. my total final bill is janky and
i looked up on multiple tutorials on how to fix it but i couldn't figure it out to save my life.


"""

import random

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'buggy'

# couple of global variables to help the code get going
import validation

LINE_LENGTH = 55
weekdays = input('What day of week were you going to be checking in again? ')


# calculates the surcharge of the room selected
def surcharge():
    sur_price = 0
    print()
    print('What type of room do you want to book?')
    room_choice = input('s=Single, d=Double, k=King: ')
    print()

    # added validation for correct guest selection
    guests = validation.get_range('How many people will be staying in the ' + room_choice + ' room? ', low=0, high=4)
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


# calculates the day of week charges
def dow_charge():
    if weekdays == 1 or 2 or 3:
        costs = 96
        return costs
    elif weekdays == 4 or 5:
        costs = 88
        return costs
    else:
        print('$80')


# displays and has all the calculations in it
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

    # i know what to do i just do not know how to do it. i
    # i have looked on tutorials but it kept going back to nonsense that i did not understand
    # added validation and are only letting people stay up to max of 7 days so we don't have squatters
    nights = validation.get_range('How many nights would you be staying? ', low=1, high=7)
    # i had major problems in regards calculating the final bill and some other stuff
    #  total = nights * (sur_price + room_choice)
    #  print('You have SUCCESSFULLY booked your stay! Your total is: ' + total)

    print("=" * LINE_LENGTH)
    input('Press any key to continue... ')
    print("=" * LINE_LENGTH)


# Can call main to see if it would run without actually running it
if __name__ == '__main__':
    hotel_rooms()
