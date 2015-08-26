class Card:
    def __init__(self, val, col):
        self.value = val
        self.color = col

    def display(self):
        print(self.value, "of", self.color)