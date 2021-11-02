#!/usr/bin/env python3

import validation as v


def list(students):
    """
    prints out the list of students and their information
    or that there are no students if the list is empty

    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :return:
    """
    if len(students) == 0:
        print('There are no students.\n')
        return

    print(f"{'ID':4s} {'First Name':20s} {'Last Name':20s}")
    print('-' * 4, '-' * 20, '-' * 20)

    for student in students:
        # <4d left align digit spacing instead of default (right align)
        print(f'{student[0]:<4d} {student[1]:20s} {student[2]:20s}')

    print()


def find_student_index(students, student_id):
    """
    Search the 2D list for a specific student ID.
    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :param student_id: student id that they user wants to find
    :type student_id: int

    :return the index of the student in the 2D list or -1 if not found
    :rtype int
    """
    for student in students:
        # student[0] looking at just id instead of all information in student
        if student_id == student[0]:
            return students.index(student)

    return -1


def add(students, next_student_id):
    """

    Add Student
    ----------
    Please enter student first name
    Please enter student last name
    Student ID # xyz was added

    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :param next_student_id:
    :return:
    """

    print('Add Student')
    print('------------')

    first_name = v.get_string('Please enter the Student\'s First Name: ').title()
    last_name = v.get_string('Please enter the Student\'s Last Name: ').title()

    # add course/sport prompt above this
    students.append([next_student_id, first_name, last_name])

    print(f'Student ID # {next_student_id} {first_name} {last_name} was added')


def update(students):
    """
    looks for student by their ID and then offers the chance to change their name
    or keep their name the same by entering no new informaiton

    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :return:
    """
    print('Update Student')
    print('------------')

    if len(students) == 0:
        print('There are no students to update')
        return

    student_id = v.get_positive('Please enter the Student ID you would like to update')

    student_index = find_student_index(students, student_id)

    if student_index == -1:
        print(f'Student ID #{student_id} not found.')
        return

    student = students[student_index]
    # confirm as a boolean instead of y/n
    confirmation = v.get_yes_no(f'Please confirm that you want to update Student ID #'
                                f'{student_id} {student[1]} {student[2]}')
    if confirmation:
        new_first_name = input(f"Please enter the Student's new first "
                               f"name or press enter to keep {student[1]}: ").title()
        if new_first_name == '':
            new_first_name = student[1]

        new_last_name = input(f"Please enter the Student's new last name "
                              f"or press enter to keep {student[2]}: ").title()
        if new_last_name == '':
            new_last_name = student[2]

        if new_first_name == student[1] and new_last_name == student[2]:
            print('Name was not changed')
        else:
            print(f'Student ID #{student_id} {student[1]} {student[2]} was updated to '
                  f'{new_first_name} {new_last_name}')

        student[1] = new_first_name
        student[2] = new_last_name
    else:
        print('Update was canceled')


def delete(students):
    """
    looks through students for a specified ID and after user confirmation
    deletes the student and their information from the list

    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :return:
    """
    print('Delete Student')
    print('------------')

    if len(students) == 0:
        print('There are no students to delete')
        return

    student_id = v.get_positive('Please enter the Student ID you would like to delete')

    student_index = find_student_index(students, student_id)

    if student_index == -1:
        print(f'Student ID #{student_id} not found.')
        return

    student = students[student_index]
    # confirm as a boolean instead of y/n
    confirmation = v.get_yes_no(f'Please confirm that you want to delete Student ID #'
                                f'{student_id} {student[1]} {student[2]}')

    if confirmation:
        students.pop(student_index)
        print(f'Student ID #{student_id} {student[1]}, {student[2]} was deleted')
    else:
        print('Delete was canceled')
