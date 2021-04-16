import random
import itertools
from termcolor import colored

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = min(self.rank,10)


    def __str__(self):
        return Card.rankName(self.rank) + self.suit


    def __int__(self):
        return self.value


    def __lt__(self, card):
        if self.rank != card.rank:
            return self.rank<card.rank
        else:
            return Card.suits().index(self.suit) > Card.suits().index(card.suit)


    def coloredString(self):
        if self.suit == "♥" or self.suit == "♦":
            color = 'red'
        else:
            color = 'grey'
        return colored(str(self), color, 'on_white')


    def rankName(rank):
        if rank == 1:
            return "A"
        elif rank < 10:
            return str(rank)
        elif rank == 10:
            return "T"
        elif rank == 11:
            return "J"
        elif rank == 12:
            return "Q"
        elif rank == 13:
            return "K"


    def suits():
        return ["♠", "♥", "♦", "♣"]


    def ranks():
        return range(1, 14)


class Deck:
    def __init__(self, cards=None):
        """
        returns a deck containing the passed cards
        if None are passed, a brand new deck is created
        """
        self.cards = []
        if cards == None:
            for suit in Card.suits():
                for rank in Card.ranks():
                    self.cards.append(Card(suit, rank))
        else:
            for card in cards:
                self.cards.append(card)


    def shuffle(self):
        random.shuffle(self.cards)


    def sort(self):
        self.cards.sort()


    def draw(self, number:int=1):
        drawn = []
        for i in range(number):
            drawn.append(self.cards.pop())
        return Deck(drawn)


    def sum(self):
        sum = 0
        for card in self.cards:
            sum += int(card)
        return sum


    def run(self):
        """
        determins if the deck contains a run
        The whole deck must be one run with no interuptions
        """
        for pos in range(len(self)):
            if self.cards[pos].rank != self.cards[0].rank + pos:
                return False
        return True


    def suits(self):
        """
        Returns all the suits found in the deck
        """
        suits = []
        for card in self.cards:
            if card.suit not in suits:
                suits.append(card.suit)
        return suits


    def combinations(self, size=None, end=None):
        """
        Returns all the possible combinations of subDecks
        A hand of 4 cards has 4 subdecks with 1 card, 6 with 2, 4 with 3, 1 with 4
        """
        if isinstance(size, int) and isinstance(end, int):
            range_ = range(size,end+1)
        elif isinstance(size, int):
            range_ = range(size,size+1)
        else:
            range_ = range(1, len(self)+1)

        combos = []
        self.sort()
        for length in range_:
            for combo in itertools.combinations(self.cards, length):
                combos.append(Deck(combo))
        return combos


    def __len__(self):
        return len(self.cards)


    def __add__(self, deck):
        newDeck = Deck(self.cards)
        for card in deck.cards:
            newDeck.cards.append(card)
        return newDeck


    def __sub__(self, deck):
        toRemove = [str(card) for card in deck.cards]
        cards = [card for card in self.cards if str(card) not in (toRemove)]
        return Deck(cards)


    def __str__(self):
        string = "("
        for card in self.cards:
            string += str(card) + ", "
        string = string[:-2] + ")"
        return string


    def coloredString(self):
        string = colored("")
        for card in self.cards:
            string += card.coloredString()
        return string
