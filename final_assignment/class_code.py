#!/usr/bin/env python3

"""
I followed along ot a youtube video and the links to which he explained how this part of the code worked and i tweaked
it to make it follow the guidelines and it work with the program as debby wanted.
With the code i programmed 3 different classes to handle all of the code.
i used a dictionary to hold the values of the cards.
I also want to point out that yes some of this code is reused, but i fully understand where it was coming from and how
it was coded. I was just kinda lazy in the aspect of doing it.

"""

import random

__author__ = 'Noah Beebe'
__copyright__ = 'Copyright 2021, CSC365'
__version__ = '1.0.1'
__status__ = 'In Progress'

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# This is here because the code did not like it being commented out or placed anywhere else but here so i said screw it
# it is going here.
playing = True

# creating card class


class Card:
    """
    the card class calls in the dictionaries and the lists of the suits and ranks to assign them to a ranking and
    to help the return in the console output of the code.
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


# creating Deck, shuffle function and single dealing#

class Deck:
    """
    Another class used to handle the deck of 52 cards practically.
    The first function helps the deck start off with an empty list that will hold the values of the random card assigned
    to the list.
    The second third and fourth one is used for adding cards to the deck as a string and then shuffling the cards
    to get that 'random' aspect of it. and the Fourth one is used to pop the cards out of the deck once they have been
    assigned to the player or dealer.
    """
    def __init__(self):
        self.deck = []  # start with an empty list#
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # starting competition deck empty#
        for card in self.deck:
            deck_comp += '\n' + card.__str__()  # add each card objects string
        return 'The deck has' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# created another class bc i found it more useful to do it this way in my head
# creating a hand


class Hand:
    """
    has 3 main functions where it makes a deck of cards with no values at the start
    and some extra code to help handle for the ace.
    """
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# creating Chips balance for competitor#

class Chips:
    """
    I created 3 different functions to help with chip handling.
    The code has it set for $1 but i assigned it to 100 for simplification because then its like penny buys
    I always played penny nickel and dime poker with my grandpa so i figured i would use that same kinda
    logic with this program.
    """
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
