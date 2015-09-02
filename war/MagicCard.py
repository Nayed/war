from Card import Card

class MagicCard(Card):
    '''Testing a magic card thing like game'''

    def getIllustration(self):
        return self.__illustration

    def setIllustration(self, illustration):
        self.__illustration = illustration

    illustration = property(getIllustration, setIllustration)

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    description = property(getDescription, setDescription)

    def getAttack(self):
        return self.__attack

    def setAttack(self, attack):
        self.__attack = attack

    attack = property(getAttack, setAttack)

    def getLifePoint(self):
        return self.__life_point

    def setLifePoint(self, life_point):
        self.__life_point = life_point

    life_point = property(getLifePoint, setLifePoint)

    def __init__(self, price, mana, illustration, description, attack = None, life_point = None):
        Card.values = (0, 1, 2, 3, 4, 5, 6)
        Card.colors = ("lowland", "island", "mountain", "forest", "marshland")
        super().__init__(price, mana)
        self.__illustration = illustration
        self.__description = description
        self.__attack = attack
        self.__life_point = life_point

    @staticmethod
    def validation(price, mana):
        if mana not in Card.colors:
            print("Error:\t {} is not a valid mana".format(mana))
            exit(1)
        if price < 0 or price > 6:
            print("Error:\t values must be between 0 and 6")
            exit(1)

    def __str__(self):
        return "Card {} : {}".format(self.color, self.description)