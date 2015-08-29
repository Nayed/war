from Deck import Deck

if __name__ == '__main__':
    c = Deck()
    c.shuffle()
    print("first card is ")
    print(c.pull())