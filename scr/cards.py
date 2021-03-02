import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return Card.rankName(self.rank) + " of " + self.suit

    def rankName(value):
        if value == 1:
            return "A"
        elif value < 10:
            return str(value)
        elif value == 10:
            return "T"
        elif value == 11:
            return "J"
        elif value == 12:
            return "Q"
        elif value == 13:
            return "K"

    def suits():
        return ["Spades", "Hearts", "Diamonds", "Clubs"]

    def ranks():
        return range(1, 14)


class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.suits():
            for rank in Card.ranks():
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self, number=1):
        drawn = []
        for i in range(number):
            drawn.append(self.deck.pop())
        return drawn

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    hand = deck.draw(5)
    for card in hand:
        print(card)
