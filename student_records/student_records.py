#!/usr/bin/env python3

def display_menu():
    print('Student Records Program')
    print()
    print('COMMAND MENU')
    print('list(1) - List all students')
    print('add(2) -  Add a student')
    print('del(3) -  Delete a student')
    print('find(4) - Find a student')
    print('exit(0) - Exit program')
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
    name = input('Name: ')
    year = input('Year: ')
    price = input('Price: ')
    student = []
    student.append(name)
    student.append(year)
    student.append(price)
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
        if command == 1:
            list(student_list)
        elif command == 2:
            add(student_list)
        elif command == 3:
            delete(student_list)
        elif command == 4:
            find_by_year(student_list)
        elif command == 0:
            break
        else:
            print('Not a valid command. Please try again.\n')
    print('Bye!')


if __name__ == '__main__':
    main()
