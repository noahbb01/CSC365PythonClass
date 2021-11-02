#!/usr/bin/env python3

import student_maintenance as maint
import validation

_author_ = 'Donaven Harrington & Noah Beebe'
_date_ = 'November 1, 2021'
_status_ = 'In Progress'


def display_menu():
    """
    prints display menu of options in the program

    :return:
    """
    print('Student Menu')
    print('======================')
    print("1 - List all students' records")
    print('2 - Add a student/sport/course')
    print('3 - Update a student/sport/course')
    print('4 - Delete a student/sport/course')
    print('5 - Exit program')


def main():
    """
    gives the menu functionality in conjunction with maintenance to
    run the options provided

    :return:
    """
    students = []
    next_student_id = 1
    valid_courses = ('history', 'math', 'science', 'english')
    valid_sports = ('football', 'track', 'volleyball', 'basketball')

    while True:
        display_menu()
        command = validation.get_range('Please enter a menu option', 1, 5)
        if command == 1:
            maint.list(students)
        elif command == 2:
            maint.add(students, next_student_id)
            next_student_id += 1
        elif command == 3:
            maint.update(students)
        elif command == 4:
            maint.delete(students)
        elif command == 5:
            break
        else:
            print("Not a valid command. Please try again.\n")
        input('Press the enter key to continue...')

    print("Bye!")


if __name__ == "__main__":
    main()
