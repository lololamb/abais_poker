# Cette classe représente un joueur


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hand = []
        self.current_status = "Alive"

    def add_cards(self, aCard):
        self.holecards.append(aCard)



