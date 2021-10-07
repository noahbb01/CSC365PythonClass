# !/usr/bin/env python3

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'Unknown'


def get_range(prompt, low, high, data_type='str'):
    """
    Defines the get range function that can be used universally. Basically it tells the user to enter a day
    in the accessible range. and if they do not, then the definition keeps running until user enters a day.
    :param prompt:
    :param low:
    :param high:
    :param data_type:
    :return:
    """
    while True:
        user_input = input(f'{prompt} (Range {low}-{high}): ')

        if data_type == 'str':
            day = int(user_input)
        else:
            day = float(user_input)

        if low < day <= high:
            return day
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)


def get_positive_num(prompt, data_type='int'):
    """
    Defines the get positive number thing. Ensures whenever it is used that the user has inputted a positive number.
    code below validates if the number entered is a positive number
    """
    while True:
        user_input = int(input(f'{prompt}: '))

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if number > 0:
            print()
            return True
        else:
            print('Entry must be greater than 0.')


"""
    This was my initial code to figure out the positive number but i thought a wee bit harder and got the above
    code to work way much better. 
      #  if user_input > 0:
      #      return print('Positive Number. ')
      #  else:
      #      return print('Negative Number. Please try again. ')
"""


def get_num(prompt):
    """
    code i first used for the get num but the code i researched over
    i found to be quite more useful.
    while True:
            user_input = int(input(f'{prompt}: '))

            if type(user_input) == int:
                return True
            else:
                print('Not a number.')
    """
    while True:
        # I understand why it says its not being used but like it looks nice right here.
        try:
            user_input = int(input(f'{prompt}: '))
        except ValueError:
            continue
        else:
            print('Good number.')
            return True


def main():
    """
    Main code for the validation module
    I did this :)
    """
    choice = "y"
    while choice.lower() == "y":
        # get input
        valid_number = get_range(prompt='Enter float', low=0, high=1000, data_type='float')
        print("Valid float = ", valid_number)
        print()
        valid_number = get_range(prompt='Enter int', low=0, high=1000, data_type='int')
        print("Valid integer = ", valid_number)
        print()
        valid_number = get_positive_num(prompt='Enter a positive number', data_type='int')
        print(valid_number)
        print()
        valid_number = get_num(prompt='Please enter a number')
        print(valid_number)
        print()

        # see if the user wants to continue
        choice = input("Repeat? (y/n): ")
        print()

    # prompts the user to have a nice day maybe
    print("Bye!")


if __name__ == "__main__":
    main()
