class Card:
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suitNum, valueNum):
        self.cardSuit = Card.suit[suitNum]
        self.cardValue = Card.value[valueNum]

    def __repr__(self):
        return f"{self.cardValue} of {self.cardSuit}"

