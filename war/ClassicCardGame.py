from CardGame import CardGame
from Card import Card

class ClassicCardGame(CardGame):
    def __init__(self):
        super().__init__()

    def initialize(self):
        for val in range(2, 15):
            for col in range(4):
                self.cards.append(Card(val, col))
        