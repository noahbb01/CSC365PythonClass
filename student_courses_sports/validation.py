#!/usr/bin/env python3
"""
Takes user input and validates the number
"""


def get_range(prompt, min, max, data_type='int'):
    """

    :param prompt:
    :param min:
    :param max:
    :param data_type:
    :return: numbers within the defined parameters
    """
    while True:
        user_input = input(f'{prompt} ({min}-{max}): ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if min <= number <= max:
            return number
        else:
            print("Entry must be greater than or equal to", min,
                  "and less than or equal to", max)


def get_positive(prompt, data_type='int'):
    """
    :param prompt:
    :param data_type:
    :return: positive numbers
    """
    while True:
        user_input = input(f'{prompt}: ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if number > 0:
                return number
            else:
                print("Entry must be greater than 0")

        except ValueError:
            print('Invalid Input: Please enter a number')


def get_response(prompt, str1, str2, ):
    """
    checks for validation of a string even upper and lower case
    :rtype: object
    :param str1:
    :param str2:
    :param prompt:
    :return: what ever number the user entered
    """
    while True:
        user_response = input(f'{prompt} ({str1}/{str2}): ')
        str1.lower()
        str2.lower()

        if user_response == str1 or user_response == str2:
            return user_response
        elif user_response.lower() == str1 or user_response.lower() == str2:
            return user_response.lower()
        elif user_response.upper() == str1 or user_response.upper() == str2:
            return user_response.upper()
        else:
            print("Answer must be ", str1, "or ", str2)


def get_string(prompt):
    """
    :param prompt:
    :return: positive numbers
    """
    while True:
        user_input = input(f'{prompt}: ')

        if user_input > '':
            return user_input
        else:
            print(f'Invalid Input: Please enter a value')


def get_number(prompt, data_type='int'):
    """
    :param prompt:
    :param data_type:
    :return: what ever number the user entered
    """
    while True:
        user_input = input(f'{prompt}')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)
        return number


def get_yes_no(prompt):
    while True:
        if prompt == '':
            user_input = input('(y=yes|n=no): ').lower()
        else:
            user_input = input(f'{prompt} (y=yes|n=no): ').lower()

        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print('Invalid Input: Please enter a y=yes, or n=no')


# a testing function to see if the data is validated
def main():
    choice = "y"
    while choice.lower() == "y":
        # get input
        print("Get range check")
        valid_number = get_range("Enter float: ", min=0, max=1000, data_type='float')
        print("Valid number = ", valid_number)
        print()
        valid_number = get_range("Enter int: ", min=0, max=1000, data_type='int')
        print("Valid integer = ", valid_number)
        print()
        print("Get positive check")

        valid_number = get_positive("Enter float: ", data_type='float')
        print("Valid number = ", valid_number)
        print()
        valid_number = get_positive("Enter int: ", data_type='int')
        print("Valid number = ", valid_number)
        print()
        print("Get number check")

        valid_number = get_number("Enter float: ", data_type='float')
        print("Valid number = ", valid_number)
        print()
        valid_number = get_number("Enter int: ", data_type='int')
        print("Valid number = ", valid_number)
        print()

        print('Get letter check')
        valid_response = get_response("Yes or No?", str1='Y', str2='N')
        print("Valid response = ", valid_response)
        print()

        # see if the user wants to continue
        choice = input("Repeat? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
