from Card import Card
import random

class Deck():

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    cards = []
    def __init__(self):
        
        for suit in Deck.suits:
            for rank in Deck.ranks:
                Deck.cards.append(Card(suit, rank))


    def shuffle(self):
        
        return random.shuffle(self.cards)
    
    def deal(self):
            return Deck.cards.pop()


