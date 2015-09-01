from Deck import Deck
from Card import Card

if __name__ == '__main__':
    c = Card(12, 2)
    deck = Deck()
    deck + c 
    print(deck)
    