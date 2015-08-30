from Deck import Deck

class DeckPlayer(Deck):

    def __init__(self):
        super().__init__(True)

    def add(self, card):
        self.cards.append(card)

    def __add__(self, card):
        self.add(card)
        