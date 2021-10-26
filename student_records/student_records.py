#!/usr/bin/env python3

"""
This program is made to add, delete, list, etc all the stuff the user inputs for a record of students
the program prompts the user to add a first and last name and then adds the input into a list
the list then can be accessed by pressing '1' and it will display all the students added with a student ID0
"""

# the follow are module level metadata for the authorship information
__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__status__ = 'Under Construction'


def display_menu():
    print('Student Records Program')
    print()
    print('COMMAND MENU')
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Delete a student')
    print('4 - Find a student')
    print('0 - Exit program')
    print()


def list(student_list):
    if len(student_list) == 0:
        print('There are no students in the list.\n')
        return
    else:
        i = 0
        for student in student_list:
            row = student
            print(str(i + 1) + '. ' + row[0]
                  + ' (' + str(row[1]) + ')'
                  + ' @ ' + str(row[2]))
            i += 1
        print()


def add(student_list):
    name = input('Please enter first name: ')
    lname = input('Please enter last name : ')
    student = []
    student.append(name)
    student.append(lname)
    student_list.append(student)
    print(student[0] + ' was added.\n')


def delete(student_list):
    number = int(input('Number: '))
    if number < 1 or number > len(student_list):
        print('Invalid student number.\n')
    else:
        student = student_list.pop(number - 1)
        print(student[0] + ' was deleted.\n')


def find_by_year(student_list):
    year = int(input('Year: '))
    for student in student_list:
        if student[1] == year:
            print(student[0] + ' was released in ' + str(year))
    print()


def main():
    student_list = []

    display_menu()
    while True:
        command = input('Command: ')
        if command == '1':
            list(student_list)
        elif command == '2':
            add(student_list)
        elif command == '3':
            delete(student_list)
        elif command == '4':
            find_by_year(student_list)
        elif command == '0':
            break
        else:
            print('Not a valid command. Please try again.\n')
    print('Bye!')


if __name__ == '__main__':
    main()
