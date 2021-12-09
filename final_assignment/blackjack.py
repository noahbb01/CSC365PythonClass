#!/usr/bin/env python3

"""
This is the meat and potatoes of the code that makes the blackjack game program what it is. It uses the same 3 diction
aries and lists just like class code just because i like to keep it the same. There is where the taking bets code is loc
as well ass hit and the hit/stands and to figure out if the user won the round or if the dealer won the hand. There is
where all of the logic takes place. This is the brain power. This is the cadillac of blackjack code. The bees knees.

"""

from class_code import *
import main

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'In Progress'

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

# playing = True

# Taking bets#


def take_bet(chips):
    """
    the logic continues to go through by making the user input a number 1-100 to get it going. It then stores the
    information that the user inputted into the chips bet value
    :param chips:
    :return:
    """
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?  '))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed {} '.format(chips.total))
            else:
                break

            # taking hits#


def hit(deck, hand):
    """
    used to see if the user wants to hit for another card
    :param deck:
    :param hand:
    :return:
    """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# player to take hits or stand#


def hit_or_stand(deck, hand):
    """
    used to see if the user wants to hit or stand. and if they enter h for hit then it will give them another
    and keep prompting them for h or s after h until the player busts or presses s.
    :param deck:
    :param hand:
    :return:
    """
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


# functions to display cards#

def show_some(player, dealer):
    """
    used to display the cards in a formatted manner that made more sense to me.
    the logic used just seemed to wrap better in my head
    :param player:
    :param dealer:
    :return:
    """
    print("\nDealer's Hand")
    print("<card hidden>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n')


def show_all(player, dealer):
    """
    used to display at the end of the dealers turn to show what cards everyone had.
    Just like in Casino Royale with Agent 007
    :param player:
    :param dealer:
    :return:
    """
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("Player's Hand = ", player.value)
