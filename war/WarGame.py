from Player import Player
from ClassicCardGame import ClassicCardGame

class WarGame:

    def __init__(self, player):
        self.__player = player
        self.__computer = Player('9000', 'HAL')
        self.__game = ClassicCardGame()

    def begin(self):
        self.__shuffle()
        self.__distribute()

        play = True
        while play:
            play = self.__main()

    def __shuffle(self):
        self.__game.shuffle()

    def __distribute(self):
        for i in range(len(self.__game.cards)):
            card = self.__game.pull()
            if i % 2 == 0:
                self.__player.addCard(card)
            else:
                self.__computer.addCard(card)
    
    def __main(self, remainder = []):
        player_card = self.__player.pullCard()
        computer_card = self.__computer.pullCard()

        if player_card is None:
            self.endGame(self.__player, self.__computer)
            return False
        elif computer_card is None:
            self.endGame(self.__computer, self.__player)
            return False

        print('Main : ')
        print('     - {} {} : {}'.format(
            self.__player.first_name, self.__player.last_name, str(player_card)))
        print('     - {} {} : {}'.format(
            self.__computer.first_name, self.__computer.last_name, str(computer_card)))

        if player_card.value == computer_card.value:
            remainder.append(player_card)
            remainder.append(computer_card)
            return self.__war(remainder)
        elif player_card.value > computer_card.value:
            self.__player.addCard(player_card)
            self.__player.addCard(computer_card)
            print('     {} {} wins'.format(self.__player.first_name, self.__player.last_name))
        else:
            self.__computer.addCard(computer_card)
            self.__computer.addCard(player_card)
            print('     {} {} wins'.format(self.__computer.first_name, self.__computer.last_name))

        return True

    def __war(self, remainder):
        print('***WAR***')
        return self.__main(remainder)

    def endGame(self, looser, winner):
        looser.defeats += 1
        winner.victories += 1
        print('{} {} won!!!'.format(winner.first_name, winner.last_name))
