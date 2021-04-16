from termcolor import colored
from cribbage import Cribbage
from cards import Card, Deck

class Player():
    """
    Contains the functions needed for the AI player to play the game
    """

    def __init__(self, name="AI Player"):
        self.name = name
        self.points = 0
        self.hand = None
        self.pile = None
        self.kitty = None


    def deal(self, cards, isDealer):
        """
        The AI is delt 6 cards, and trys to select 4 to keep,
        and the 2 that will go into the kitty
        """
        if len(cards) != 6:
            raise ValueError("hand must be six cards")

        remaining = Deck() - cards

        hands = []
        for hand in cards.combinations(4):
            handValue = {
                "hand": hand,
                "pointsSum": 0,
                "points": []
            }
            kitty = cards-hand
            pointsKitty = Cribbage.pointsKitty(kitty)

            for card in remaining.combinations(1):
                points, _ = Cribbage.points(hand, card, False)

                if isDealer:
                    points += pointsKitty
                else:
                    points -= pointsKitty

                handValue["pointsSum"]+=points
                handValue["points"].append(points)
            hands.append(handValue)

        # selects the hand that likely to give the most points
        seq = [hand['pointsSum'] for hand in hands]
        best = seq.index(max(seq))

        self.hand = hands[best]['hand']
        self.kitty = cards - self.hand
        self.pile = Deck([])

        print(self.name + "\tHand: ", end="")
        print(self.hand.coloredString(), end="")
        print("\tKitty: ", end="")
        print(self.kitty.coloredString())


    def score(self, face, kitty=None):
        """
        Is used to score the hand of the player
        will score the kitty if applicable
        """
        points, pString = Cribbage.points(self.pile, face)
        endString = colored(" with the hand: ")
        endString += self.pile.coloredString()
        endString += colored("+")
        endString += face.coloredString()

        self.addPoints(points, endString)

        if kitty is not None:
            points, pString = Cribbage.points(kitty, face, True)
            endString = colored(" from the kitty: ")
            endString += kitty.coloredString()
            endString += colored("+")
            endString += face.coloredString()
            self.addPoints(points, endString)


    def play(self, pile):
        """
        The player will try to play a card from hand to the pile
        """
        if len(self.hand.cards) > 0:

            plays = []
            for card in self.hand.cards:
                card = Deck([card])
                newPile = pile + card
                if newPile.sum() <= 31:
                    play = {
                        "card": card,
                        "points": Cribbage.pointsPegging(newPile)
                    }
                    plays.append(play)

            if len(plays) > 0:
                seq = [play['points'] for play in plays]
                best = seq.index(max(seq))

                card = plays[best]["card"]
                self.pile += card
                self.hand -= card
                return card

        print(self.name + " couldn't play")
        return None



    def addPoints(self, points, using):
        """
        Adds the points to the player
        If the player has more than 120 points,
        they win the game, and inturupt the loop
        """
        self.points += points
        scored = colored(self.name + " scored " + str(points) + " points", 'grey', 'on_green')
        total = colored(" (" + str(self.points) + ")", 'red', 'on_green')
        print(scored + total + using)

        if self.points >= 121:
            string = colored(self.name + " has won with " + str(self.points) + " points!", 'grey', 'on_yellow')
            raise ValueError(string)
