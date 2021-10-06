# !/usr/bin/env python3

"""
Created by: Noah Beebe
Date: 9/2/2021
Cover Crop Calculator: use this program to figure out how much of a certain cover crop you
need to cover your field.

As of 10/6/2021: Added validation check code to ensure data integrity
And yes I coded this all in one day.
"""

import validation

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__credits__ = ['Noah Beebe']
__version__ = '1.0.1'
__maintainer__ = 'Noah Beebe'
__email__ = 'nobeeb01@wsc.edu'
__status__ = 'Finished'


def cover_crop_calc():
    # display a welcome message
    print("Cover Crop Calculator")
    print()

    print("Estimated Cover Crop Area")
    print()

    # get input from the user
    # added validation to ensure user puts in a positive number
    field_length = validation.get_positive_num("Enter length of field in terms of feet:\t\t")
    field_width = validation.get_positive_num("Enter width of field in terms of feet:\t\t")

    # calculate total area of field
    area = field_length * field_width
    area = round(area, 2)

    # calculates the amount of acres based off of the users input
    acre = area / 43560

    # gets input from the user for the seeding rate based off of whatever crop they are going to use
    # added validation to ensure user puts in a positive number
    seeding_rate = validation.get_positive_num("Enter seeding rate in terms of pounds:\t\t")

    # calculates the amount of cover crop needed by taking seeding rate times acre
    cover_crop = seeding_rate * acre

    # format and display the result
    print()
    print("Estimated Area of Field:\t" + str(area))
    print()
    print("Estimated Acreage of Field:\t" + str(acre))
    print()
    print("Estimated amount of cover crop needed:\t" + str(cover_crop))
    print()
    print("Bye")


# checks to see if this is running without actually running it
if __name__ == '__main__':
    cover_crop_calc()
