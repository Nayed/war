class Card:
    values = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "As")
    colors = ("Heart", "Diamonds", "Clubs", "Spades")

    def __getValue(self):
        return self.__value

    def __setValue(self, val):
        self.__value = val

    value = property(__getValue, __setValue)

    def __init__(self, val, col):
        if val < 2 or val > 14:
            print("Error: \n\tValue must be between 2 and 14")
            exit(1)
        if col < 0 or col > 3:
            print("Error: \n\tCode color must be between 0 and 3")
            exit(1)
        self.__value = val
        self.__color = col

    def __str__(self):
        return str(Card.values[self.__value]) + " of " + Card.colors[self.__color]

    def display_ascii(self):
        name = str(Card.values[self.__value]) + " of " + Card.colors[self.__color]
        size = len(name) + 2
        print("/", "-" * size, "\\", sep="")
        print("|", name, "|")
        print("|", "-" * size, "|", sep="")
        print("\\", "-" * size, "/", sep="")