class Card:

    values = None
    colors = None

    def getValue(self):
        return self.__value

    def setValue(self, val):
        self.__value = val

    value = property(getValue, setValue)

    def getColor(self):
        return self.__color

    def setColor(self, col):
        self.__color = col

    color = property(getColor, setColor)

    def __init__(self, val, col):
        if self.__class__ is Card:
            raise Exception("Creation forbidden!")
        self.__class__.validation(val, col)
        self.__value = val
        self.__color = col

    def __str__(self):
        return str(Card.values[self.value]) + " of " + Card.colors[self.color]

    def display_ascii(self):
        name = str(Card.values[self.value]) + " of " + Card.colors[self.color]
        size = len(name) + 2
        print("/", "-" * size, "\\", sep="")
        print("|", name, "|")
        print("|", "-" * size, "|", sep="")
        print("\\", "-" * size, "/", sep="")

    @staticmethod
    def validation(val, col):
        pass