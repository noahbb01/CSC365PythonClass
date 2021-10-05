# !/usr/bin/env python3

"""
This code is being used along with the other.. hang on lemme count.....7? No. Oh, my bad there is four other
programs located in this project.
This program pulls in hte other four farm related calculators and we turned it into a menu option to choose
which program you would like to run all in one handy place.

Now at this point there is an error saying 'Cannot find reference to my break even and cover crop calculator', but
the program runs with no issues, so I have zero clue what is going on with it.
"""

import break_even_calc as bec
import cover_crop_calc as ccc
import stocking_rate_calc as src
import water_allocations_calc as wac

# the follow are module level metadata for the authorship information
__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__credits__ = ['Noah Beebe']
__version__ = '1.0.1'
__maintainer__ = 'Noah Beebe'
__email__ = 'nobeeb01@wsc.edu'
__status__ = 'Production/Almost Finished'

# Global variable used for formatting in the code
LINE_LENGTH = 40


# Displays the print out of the other farm calculators and the number associated with
def display_menu():
    print("The Farmers Calculators ")
    print("=" * LINE_LENGTH)
    print("COMMAND MENU")
    print('1- Break Even Calculator ')
    print('2- Cover Crop Calculator ')
    print('3- Stocking Rate Calculator ')
    print('4- Water Allocations Calculator ')
    print('5- Help ')
    print('0- Exit Program ')
    print()


# Well obviously this is the main. And it is the bee's knees when it comes to running this menu program
def main():
    while True:
        display_menu()
        command = input('Command: ')
        # The code listed below assigns each farm calc to a number that the user can select to choose which
        # calculator that best fits their needs
        if command == "1":
            bec.break_even_calc()
        elif command == "2":
            ccc.cover_crop_calc()
        elif command == "3":
            src.stocking_rate_calc()
        elif command == "4":
            wac.water_allocations_calc()
        elif command == "0":
            break
        # Supposed to show the docstring from each farm calc
        elif command == "5":
            print('help')
        else:
            print('Not a valid command. Please try again.\n')
        print()

        print("=" * LINE_LENGTH)
        input('Press any key to continue... ')
        print("=" * LINE_LENGTH)

    print('Bye!')


# Can call main to see if it would run without actually running it
if __name__ == '__main__':
    main()
