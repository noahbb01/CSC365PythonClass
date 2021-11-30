#!/usr/bin/env python3

"""
Docstring this when ready

"""
# import validation

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'In Progress'


def display_menu():
    # the point of this function is to easily display the commands available to the user to type in
    print(f'=========================================================================')
    print(f'Welcome to Game 21')
    print(f'=========================================================================')
    print(f'The rules are simple!')
    print(f'1. Each player is trying to get as close to 21 without going over.')
    print(f"2. Each player is ONLY trying to beat the dealer's hand.")
    print(f'3. The dealer will keep dealing himself cards')
    print(f'until he beats all players hands or goes over 21.')
    print(f'4. Tie goes to the player, not the dealer.')
    print(f'5. Each player gets dealt two card between 1 - 10.')
    print(f'6. The player then can choose to receive additional cards.')
    print(f'7. Each player starts with $1.00.')
    print(f'8. Default bet is 25 cents, but the player can double it after holding.')
    print(f'9. Winner is the last person with cash, not including the dealer.')
    print(f'=========================================================================')


def main():
    display_menu()


if __name__ == '__main__':
    main()
