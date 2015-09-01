from Card import Card
import random

class CardGame:
    def __getCards(self):
        return self.__cards

    def __setCards(self, card):
        if len(self.__cards) > 52:
            raise Exception("Deck full")
        self.__cards.append(card)

    cards = property(__getCards, __setCards)

    def __init__(self, empty = False):
        self.__cards = []

        if not empty:
            for val in range(2, 15):
                for col in range(4):
                    self.__cards.append(Card(val, col))

    def __str__(self):
        game_cards = ""
        for card in self.cards:
            if game_cards == "":
                game_cards = str(card)
            else:
                game_cards += ", " + str(card)
        return game_cards

    def shuffle(self):
        random.shuffle(self.cards)

    def pull(self):
        try:
            return self.cards.pop(0)
        except IndexError as error:
            print("There is no card left!")
            return None
            