from WarGame import WarGame
from Player import Player

if __name__ == '__main__':
    player_1 = Player('Kanye', 'West')
    game = WarGame(player_1)
    game.begin()
    