from Card import Card

class ClassicCard(Card):

    def __init__(self, val, col):
        Card.values = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "As")
        Card.colors = ("Heart", "Diamonds", "Clubs", "Spades")
        super().__init__(val, col)

    @staticmethod
    def validation(val, col):
        if val < 2 or val > 14:
            print("Error:\tValue must be between 2 and 14")
            exit(1)
        if col < 0 or col > 3:
            print("Error:\tCode color must be between 0 and 3")
            exit(1)
