#!/usr/bin/env python3

"""
The main function of this file is to provide the main program with the functions it needs to succeed
we have the list function where the user presses 1 and it will pull up all the students added in the list
the add function where you can add students
delete function where you can delete students

"""
import validation


def lists(student_list):
    """

    :param student_list:
    :return:
    """
    if len(student_list) == 0:
        print('There are no students.\n')
        return

    print(f"{'ID':4s} {'First Name':20s} {'Last Name':20s}")
    print('-' * 4, '-' * 20, '-' * 20)

    for student in student_list:
        # print(student[0], student[1], student[2])
        print(f'{student[0]:<4d} {student[1]:20s} {student[2]:20s}')
        print()


def add(student_list, next_student_id):
    """
    Add Student
    -----------
    Please enter the Student's First Name: mary jean
    Please enter the Student's Last Name: smith
    Student ID #1 Mary Jean Smith was added.
    Press Enter to continue...
    """
    print()
    print('ADD STUDENTS')
    print()
    name = validation.get_string("Please enter the Student's first name").title()
    lname = validation.get_string("Please enter the Student's last name").title()
    print()

    student_list.append([next_student_id, name, lname])

    print(f'Student ID #{next_student_id} {name} {lname} was added.')
    print()


def delete(student_list):
    """

    :param student_list:
    :return:
    """
    if len(student_list) == 0:
        print('There are no students in the database.\n')
        return

    student_id = validation.get_positive_num('Please enter the Student ID you would like deleted: ')

    student_index = find_student_index(student_list, student_id)

    if student_index == -1:
        print(f'Student ID #{student_id} not found. ')
        return

    student = student_list[student_index]
    confirm = input(f'Are you sure you want to delete Student ID #{student_id} {student[1]} '
                    f'{student[2]} (y=yes, n=no): ')

    if confirm:
        student = student_list.pop(student_id - 1)
        print(f'Student ID #{student_id} {student[1]} {student[2]} was deleted.\n')
    else:
        print(f'Delete was cancelled')


def find_student_index(student_list, student_id):
    """
    :param student_list:
    :param student_id: student id that they user wants to find
    :type student_id: int

    :return the index of the student in the 2D list or -1 if not found
    :rtype int
    """
    for student in student_list:
        if student_id == student_list[0]:
            return student_list.index(student)
    return -1


def update_student(student_list):
    """
    :param student_list:
    :return:
    """
    if len(student_list) == 0:
        print('There are no students to update.\n')
        return

    student_id = validation.get_positive_num('Please enter the Student ID you would like updated: ')

    student_index = find_student_index(student_list, student_id)

    if student_index == -1:
        print(f'Student ID #{student_id} not found. ')
        return

    student = student_list[student_index]
    confirm = input(f'Are you sure you want to update Student ID #{student_id} {student[1]} '
                    f'{student[2]} (y=yes, n=no): ')

    if confirm:
        print(f'Student ID #{student_id} {student[1]} {student[2]} was updated.')
    else:
        print(f'Update was cancelled')
