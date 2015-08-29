from Card import Card
import random

class Deck:
    def __init__(self):
        self.__cards = []

        for val in range(2, 15):
            for col in range(4):
                self.__cards.append(Card(val, col))

    def __str__(self):
        game_cards = ""
        for card in self.__cards:
            if game_cards == "":
                game_cards = str(card)
            else:
                game_cards += ", " + str(card)
        return game_cards

    def shuffle(self):
        random.shuffle(self.__cards)

    def pull(self):
        try:
            return self.__cards.pop(0)
        except IndexError as error:
            print("There is no card left!")
            return None
            