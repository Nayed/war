from Player import Player
from ClassicCard import ClassicCard

if __name__ == '__main__':
    
    c = ClassicCard(2, 2)
    j1 = Player("Gaston", "Lagaffe")
    print(j1)
    j1.addCard(c)
    print(j1)