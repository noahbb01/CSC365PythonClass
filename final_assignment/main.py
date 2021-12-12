#!/usr/bin/env python3

"""
Main code in the blackjack program where the Display rules portion of code is being housed at. I understand that
it was supposed to include more than one player to play against the dealer but i found it much easier to just do one
player play against the dealer. All values are held except for the name of the player. It is simply 'Player vs. Dealer'
For some reason im just curious on is that i do not have anything called in main and it says my imports are not used
but if i leave them like how they are now the code runs as intended. But if i delete the 'unused imports', the code does
not run. I understand it a little bit im just gonna leave it because its kinda funny to me anyways.

"""
from blackjack import *

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'In Progress'


def display_rules():
    print(f'=========================================================================')
    print(f'Welcome to Game 21')
    print(f'=========================================================================')
    print(f'The rules are simple!')
    print(f'1. Each player is trying to get as close to 21 without going over.')
    print(f"2. Each player is ONLY trying to beat the dealer's hand.")
    print(f'3. The dealer will keep dealing himself cards')
    print(f'   until he beats all players hands or goes over 21.')
    print(f'4. Tie goes to the player, not the dealer.')
    print(f'5. Each player gets dealt two card between 1 - 10. With Ace being high. ')
    print(f'6. The player then can choose to receive additional cards.')
    print(f'7. Each player starts with $1.00. (100)')
    print(f'8. Default bet is however much the player wants to bet.')
    print(f'9. Winner is the last person with cash, not including the dealer.')
    print(f'=========================================================================')


def get_player_names():
    while player > 3:
        player_names = input(str('Please enter names of who is playing (Max # of players = 2): '))
        players['playerInfo'].append(player_names)


def main():
    """
    :return:
    """
    display_rules()
   # get_player_names()
    play_game()


if __name__ == '__main__':
    main()
