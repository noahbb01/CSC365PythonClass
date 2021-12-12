#!/usr/bin/env python3

"""


"""
import random

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'In Progress'

# need to allow the user to take on bets
# store player info in a dictionary? with it storing the name of the user input # final cards
# need to code for the final amounts with bets

players = {'playerInfo': []}

dealer_cards = []

player_cards = []

players['playerInfo'].append(player_cards)


def get_player_names():
    player = 0
    while player > 3:
        player_names = str(input('Please enter names of who is playing (Max # of players = 2): '))
        players['playerInfo'].append(player_names)


def play_game():
    total = 100
    bet = int(input('Please enter how much you would like to bet (0-100): '))

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
        action_taken = str(input('Do you want another one? (y=yes): '))
        print()
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
        print()
        print('Player Busted!')
        total -= bet
        print(total)
    elif sum(player_cards) == 21:
        print()
        print('Player Wins!')
        total += bet
        print(total)
