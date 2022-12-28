import random
from typing import List, Any

from .Card import *


# Cette classe représente un jeu de carte, matérialisé par un tableau de cartes.
class Deck:
    deck_cards: list[Card]

    def __init__(self):
        self.deck_cards = []

    def initialize(self):
        # write some codes for initialize the deck
        for i in range(0, 4):
            for j in range(0, 13):
                self.deck_cards.append(Card(i, j))

    def get_length(self):
        return len(self.deck_cards)

    def shuffle(self):
        shuffled_cards = []

        # write some codes for shuffle deck
        for i in range(len(self.deck_cards)):
            if len(self.deck_cards) > 1:
                c = random.choice(self.deck_cards)
                shuffled_cards.append(c)
                self.deck_cards.remove(c)
            else:
                c = self.deck_cards.pop()
                shuffled_cards.append(c)
        self.deck_cards = shuffled_cards

    def pop(self):
        return self.deck_cards.pop()

    def __str__(self):
        result = ''

        for card in self.deck_cards:
            result += card.__str__()

        result += 'size: ' + str(len(self.deck_cards))
        return result
