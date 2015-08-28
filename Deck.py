from Card import Card

class Deck:
    def __init__(self):
        self.cards = []

        for val in range(2, 15):
            for col in range(4):
                self.cards.append(Card(val, col))

    def __str__(self):
        game_cards = ""
        for card in self.cards:
            if game_cards == "":
                game_cards = str(card)
            else:
                game_cards += ", " + str(card)
        return game_cards