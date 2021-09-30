# !/usr/bin/env python3

import break_even_calc as bec
import cover_crop_calc as ccc
import stocking_rate_calc as src
import water_allocations_calc as wac

LINE_LENGTH = 40


def display_menu():
    print("The Farmers Calculators ")
    print("=" * LINE_LENGTH)
    print("COMMAND MENU")
    print('1- Break Even Calculator ')
    print('2- Cover Crop Calculator ')
    print('3- Stocking Rate Calculator ')
    print('4- Water Allocations Calculator ')
    print('5- Exit Program ')
    print('0- Help ')
    print()



def main():

    while True:
        display_menu()
        command = input('Command: ')

        if command == "1":
            bec.break_even_calc()
        elif command == "2":
            ccc.cover_crop_calc()
        elif command == "3":
            src.stocking_rate_calc()
        elif command == "4":
            wac.water_allocations_calc()
        elif command == "5":
            break
        elif command == "0":
            print('help')
        else:
            print('Not a valid command. Please try again.\n')
        print()

    print('Bye!')


if __name__ == '__main__':
    main()
