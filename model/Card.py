# Cette classe représente un carte, avec un rang et une couleur représentés pas des valeurs
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def __str__(self):
        return '(suit:' + str(self.suit) + ', rank: ' + str(self.rank) + ')'
