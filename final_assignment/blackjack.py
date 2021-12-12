#!/usr/bin/env python3

"""
The new logic behind the code. I tried coding this quickly to meet deadline date. I made two different lists
one for the dealers cards and one for the players cards. i did not make it so multiple players can play at once. Just
1v1. player vs the dealer. I then try to store the players data into a dictionary.
The code works but i got some ordering issues going on that i am trying to resolve at the moment.
The betting needs some tweak work too.
Betting works better now.
Update: Everything looks good. Just needed to implement the multiple users to play.
I do not have that code coded. I have the user type in the users who wants to play but i do not let the other users
play. I simply have it as a 1v1.

"""
import random
import validation

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'In Progress'

# need to allow the user to take on bets: DONE
# store player info in a dictionary? with it storing the name of the user input # final cards: Maybe?
# need to code for the final amounts with bets: Done?

# the dictionaries and lists used in the following code
players = {'Players': []}
dealer_cards = []
player_cards = []
players['Players'].append(player_cards)


def determine_winner():
    """
    This code is used to determine if the dealer or player busts or if the player or dealer wins.
    :return:
    """
    total = 100
    if sum(dealer_cards) == 21:
        print('Dealer has 21 and wins!')
    elif sum(dealer_cards) > 21:
        print('Dealer goes over!')

    if sum(player_cards) > 21:
        print()
        print('Player Busted!')
        total -= 25
        print('Player now has:', total)
    elif sum(player_cards) == 21:
        print()
        print('Player Wins!')
        total += 25
        print('Player now has:', total)


def play_game():
    """
    The main logic code used to provide the user with the 21 game program
    :return:
    """
    bet = validation.get_yes_no('Normal bet is 25. Would you like to bet 25? ')

    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print('Dealer has X and : ', dealer_cards[1])

    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print('Player has: ', player_cards)

    while sum(player_cards) < 21:
        action_taken = str(input('Do you want another one? (y=yes): '))
        print()
        if action_taken == 'y':
            player_cards.append(random.randint(1, 11))
            # adds a new card to the player list. I made it so they see the new card and the total of them.
            print('You now have a total of: ' + str(sum(player_cards)) + ' with your cards being ', player_cards)
        elif action_taken == 'n':
            break
        else:
            print()
            print('The dealer has a total of ' + str(sum(dealer_cards)) + ' with ', dealer_cards)
            print('Player now has a total of ' + str(sum(player_cards)) + ' with ', player_cards)

        determine_winner()
        print()
    print(players)
