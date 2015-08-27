class Card:
    values = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")
    colors = ("Heart", "Diamonds", "Clubs", "Spades")

    def __init__(self, val, col):
        if val < 2 or val > 14:
            print("Error: \n\tValue must be between 2 and 14")
            exit(1)
        if col < 0 or col > 3:
            print("Error: \n\tCode color must be between 0 and 3")
            exit(1)
        self.value = val
        self.color = col

    def __str__(self):
        return str(Card.values[self.value]) + " of " + Card.colors[self.color]

    def display_ascii(self):
        name = str(Card.values[self.value]) + " of " + Card.colors[self.color]
        size = len(name) + 2
        print("/", "-" * size, "\\", sep="")
        print("|", name, "|")
        print("|", "-" * size, "|", sep="")
        print("\\", "-" * size, "/", sep="")