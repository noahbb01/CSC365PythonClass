#!/usr/bin/env python3

"""


"""
import random

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'In Progress'


dealer_cards = []

player_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print('Dealer has X and : ', dealer_cards[1])

while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print('Player has: ', player_cards)

if sum(dealer_cards) == 21:
    print('Dealer has 21 and wins!')
elif sum(dealer_cards) > 21:
    print('Dealer goes over!')

while sum(player_cards) < 21:
    action_taken = str(input('Do you want another one? '))
    if action_taken == 'y':
        player_cards.append(random.randint(1, 11))
        # adds a new card to the player list. I made it so they see the new card and the total of them.
        print('You now have a total of: ' + str(sum(player_cards)) + ' with your cards being ', player_cards)
    else:
        print()
        print('The dealer has a total of ' + str(sum(dealer_cards)) + ' with ', dealer_cards)
        print('Player now has a total of ' + str(sum(player_cards)) + ' with ', player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print('Dealer Wins!')
        else:
            print('Player Wins!')
            break

if sum(player_cards) > 21:
    print('Player Busted!')
elif sum(player_cards) == 21:
    print('Player Wins!')

