from CardGame import CardGame

class Deck(CardGame):

    def __init__(self):
        super().__init__()

    def add(self, card):
        self.cards.append(card)

    def __add__(self, card):
        self.add(card)
        