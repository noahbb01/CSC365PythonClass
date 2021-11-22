#!/usr/bin/env python3

import csv
import validation
import sys

_author_ = 'Noah Beebe'
_date_ = 'November 17, 2021'
_status_ = 'In Progress'

my_output_data = [
    [1, 'Johnson, Debbie', [10.1, 20.25, 30.0, 40.0]],
    [4, 'Book, Mac', [11.13, 30.5, 66.1, 43.1]],
    [33, 'Bear, Teddie', [10.14, 24.2, 32.3, 3.0]]
]

FILENAME = 'my_output_data.csv'


def display_menu():
    """
    prints display menu of options in the program
    :return:
    """
    print()
    print('Python I/O and Error Handling')
    print('======================')
    print("1 - List all data un-formatted")
    print('2 - List all data formatted')
    print('3 - Exit program')


def read_file():
    write_file()
    try:
        with open("my_output_data.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0] + " " + str(row[1]) + " " + str(row[2]))
    except FileNotFoundError:
        print('Could not find ' + FILENAME + " file.")
    except Exception as e:
        print(type(e), e)
        exit_program()
    finally:
        file.close()


def write_file():
    try:
        with open("my_output_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(my_output_data)
    except Exception as e:
        print(type(e), e)
        exit_program()


def display_list():
    print(f'{"ID":>4s} {"Name":<20s} {"Data":<34s}')
    print('=' * 4, '=' * 20, '=' * 34)

    print(f'{my_output_data[0]}')
    print(f'{my_output_data[1]}')
    print(f'{my_output_data[2]}')



def exit_program():
    print('Terminating Program')
    sys.exit()


def main():
    while True:
        display_menu()
        command = validation.get_range('Please enter a menu option', 1, 3)
        print()
        if command == 1:
            read_file()
        elif command == 2:
            display_list()
        elif command == 3:
            break
        else:
            print("Not a valid command. Please try again.\n")
        print()
        input('Press the enter key to continue...')


print("Bye!")

if __name__ == "__main__":
    main()
