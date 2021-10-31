#!/usr/bin/env python3

"""
This program is made to add, delete, list, etc all the stuff the user inputs for a record of students
the program prompts the user to add a first and last name and then adds the input into a list
the list then can be accessed by pressing '1' and it will display all the students added with a student ID0

Update: as of 10/29/21 Everything seems to working right
Update: as of 10/31/21 It does not seem to find the correct student ID in the Update and the Delete portions of code
Can not figure out why it is doing it.
"""
from student_maint import *

# the follow are module level metadata for the authorship information
__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__status__ = 'Under Construction'

LINE_LENGTH = 25


def display_menu():
    # the point of this function is to easily display the commands available to the user to type in
    print('Student Records Program')
    print(LINE_LENGTH * '=')
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Delete a student')
    print('4 - Update a student')
    print('0 - Exit program')
    print()


def main():
    # main
    student_list = []
    next_student_id = 1

    while True:
        display_menu()
        command = input('Please enter a Menu #: ')
        if command == '1':
            lists(student_list)
        elif command == '2':
            add(student_list, next_student_id)
            next_student_id += 1
        elif command == '3':
            delete(student_list)
        elif command == '4':
            update_student(student_list)
        elif command == '0':
            break
        else:
            print('Not a valid command. Please try again.\n')

        input('Press enter to continue...')

    print('Bye!')


if __name__ == '__main__':
    main()
