from DeckOfCards.Card import Card
import random

class Deck:
    count = 0

    def __init__(self):
        self.deckOfcards = []
        for i in range(0, 4):
            for j in range(0,13):
                self.deckOfcards.append(Card(i,j))
        Deck.count = len(self.deckOfcards)

    def __repr__(self):
        return f"Deck of {Deck.count} cards"

    def __iter__(self):
        return iter(self.deckOfcards)
    def _deal(self,num):
        listOfCard = []
        if num <= Deck.count:
            for i in range(num):
                item = random.choice(self.deckOfcards)
                listOfCard.append(item)
                self.deckOfcards.remove(item)
            Deck.count -= num
        elif Deck.count == 0:
            raise ValueError("All cards have been dealt")
        else:
            listOfCard = self.deckOfcards[:]
            del self.deckOfcards[:]
            Deck.count = 0
        return listOfCard

    def shuffle(self):
        if Deck.count < 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            random.shuffle(self.deckOfcards)

    def deal_card(self):
        item = self._deal(1)
        if(len(item)==1):
            return item[0]
        return item

    def deal_hand(self,num):
        return self._deal(num)


    # def printCard(self):
    #     for item in self.deckOfcards:
    #         print(item)