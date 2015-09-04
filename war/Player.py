from Deck import Deck

class Player:

    def getFirstName(self):
        return self.__first_name

    first_name = property(getFirstName)

    def getLastName(self):
        return self.__last_name

    last_name = property(getLastName)

    def getVictories(self):
        return self.__victories

    def setVictories(self, n):
        self.__victories = n

    victories = property(getVictories, setVictories)

    def getDefeats(self):
        return self.__defeats

    def setDefeats(self, n):
        self.__defeats = n

    defeats = property(getDefeats, setDefeats)

    def getDeck(self):
        return self.__deck

    deck = property(getDeck)

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__victories = 0
        self.__defeats = 0
        self.__deck = Deck()

    def pullCard(self):
        return self.deck.pull()

    def addCard(self, card):
        self.deck.add(card)

    def __str__(self):
        return "{} {}\nHistory: {} defeat(s) and {} victorie(s)\n{}".format(
            self.first_name, self.last_name, self.defeats, self.victories, str(self.deck))