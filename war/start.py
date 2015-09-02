from Deck import Deck
from ClassicCard import ClassicCard

if __name__ == '__main__':
    c = ClassicCard(12, 2)
    deck = Deck()
    deck + c 
    print(deck)
    