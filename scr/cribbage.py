from cards import Card, Deck
from termcolor import colored
import player as AI

class Cribbage():
    """
    Contains all the functions for playing a game of cribbage
    """

    def points(hand, face, isCrib=False):
        """
        Counts all the points in a given crib hand
        There are slightly different flush rules for the crib
        """

        cards = hand + face
        cards.sort()
        results = []

        results.append(Cribbage.fifteens(cards))
        results.append(Cribbage.pairs(cards))
        results.append(Cribbage.runs(cards))
        results.append(Cribbage.flush(hand, face, isCrib))
        results.append(Cribbage.nob(hand, face))

        points = 0
        string = ""
        for result in results:
            points += result[0]
            string += result[1]

        return points, string

    def pointsKitty(cards):
        """
        Estimates the points for a given kitty
        """
        cards.sort()

        points = 0
        points += (Cribbage.fifteens(cards))[0]
        points += (Cribbage.pairs(cards))[0]
        if cards.run():
            points+=1

        return points


    def fifteens(cards):
        """
        Every combination of cards that adds to 15 is worth 2 points
        """
        points = 0
        string = ""
        for combo in cards.combinations():
            if combo.sum() == 15:
                points += 2
                string += "15: " + str(combo) + "\n"
        return points, string


    def pairs(cards):
        """
        Every pair of cards is worth 2 points
        3 of a kind is 6 points, since there are 3 different pairs
        """
        points = 0
        string = ""
        for combo in cards.combinations(2):
            if combo.cards[0].rank == combo.cards[1].rank:
                points += 2
                string += "pair: " + str(combo) + "\n"
        return points, string


    def runs(cards):
        """
        A run of cards is worth the length of the run
        You can have multiple runs if you have a pair of one of the values
        """
        points = 0
        string = ""
        for size in range(5,2,-1):
            for combo in cards.combinations(size):
                if combo.run():
                    points += len(combo)
                    string += "Run: " + str(combo) + "\n"
            if points > 0:
                break
        return points, string


    def flush(hand, face, isCrib):
        """
        A flush is when your hand is all the same suit, and is worth the
        size of your hand. A flush need not include the face for the normal hand,
        but the crib is only a flush if it includes the face.
        """
        points = 0
        string = ""
        if len((hand+face).suits()) == 1:
            points += 5
            string += "flush: " + str(hand+face) + "\n"
        elif not isCrib and len(hand.suits()) == 1:
            points += 4
            string += "flush: " + str(hand) + "\n"
        return points, string


    def nob(hand, face):
        """
        A Jack of the face's suit is worth 1 point
        """
        points = 0
        string = ""
        for card in hand.cards:
            if card.rank == 11 and card.suit == face.cards[0].suit:
                points = 1
                string = "nob with the " + str(card) + "\n"
        return points, string


    def pointsPegging(pile):
        """
        As players play cards to the pile, they may earn points
        This is called pegging and scores the following plus the Go
        the Go is calculated elsewhere
        """
        points = 0

        points += Cribbage.fifteensPegging(pile)
        points += Cribbage.pairsPegging(pile)
        points += Cribbage.runsPegging(pile)

        return points


    def fifteensPegging(pile):
        """
        if the sum of the pile is 15 or 31, score 2 points
        """
        if pile.sum() == 15 or pile.sum() == 31:
            return 2
        else:
            return 0


    def pairsPegging(pile):
        """
        If the played card matches the one(s) below it, score the pairs
        There cannot be any forien card interupting the pairs
        """
        rank = pile.cards[-1].rank
        count = 1

        while count < len(pile.cards) and count < 5 and pile.cards[-count-1].rank == rank:
            count += 1

        return (count-1) * count


    def runsPegging(pile):
        """
        If the played card forms a run with the ones below it, score the runs
        There cannot be any forien card interupting the run
        The run does not need to be in order
        """
        length = len(pile.cards)

        while length > 2:
            run = Deck(pile.cards[-length:])
            run.sort()
            if run.run():
                return length
            length -= 1

        return 0


    def playAIGame():
        """
        Plays a game of Cribbage using two AI players
        """

        players = [AI.Player("player 2"), AI.Player("player 1")]

        try:
            round = 1
            while(True):
                """
                players[1] is the dealer, the array order is swapped every round
                The while loop will break when one player passes 121 points
                (This is done by throwing an exeption)
                """

                deck = Deck()
                deck.shuffle()
                print("\n")
                print(colored("Round " + str(round), 'grey', 'on_yellow'))
                print("")
                print(colored("The Deal", 'grey', 'on_magenta'))
                print(players[1].name + " is the dealer")

                players[0].deal(deck.draw(6), isDealer=False)
                players[1].deal(deck.draw(6), isDealer=True)

                face = deck.draw()
                print("The face card is: ", end="")
                print(face.coloredString())
                if Card.rankName(face.cards[0].rank) == "J":
                    players[1].addPoints(2, colored(" for the face being a Jack"))

                print("")
                print(colored("The Play", 'grey', 'on_magenta'))
                Cribbage.pegging(players)

                kitty = players[0].kitty + players[1].kitty

                print("")
                print(colored("The Count", 'grey', 'on_magenta'))
                players[0].score(face)
                players[1].score(face, kitty)


                players.reverse()
                round += 1

        except ValueError as e:
            print()
            print(e)


    def pegging(players):
        """
        This performes the play for one pile
        each player plays cards until they run out, or neither can
        play on the current pile
        """
        peggingPlayers = players.copy()
        players = players.copy()
        pile = Deck([])


        while len(players[0].hand) + len(players[1].hand) > 0:
            card = peggingPlayers[0].play(pile)

            if card is not None:
                pile += card

                print(peggingPlayers[0].name + " played the ", end="")
                print(card.coloredString(), end="")
                print(colored("\tsum: " + str(pile.sum()), 'red'), end="")
                print("\tpile: ", end="")
                print(pile.coloredString())

                points = Cribbage.pointsPegging(pile)
                if points > 0:
                    string = colored(" for playing the ") + card.coloredString()
                    peggingPlayers[0].addPoints(points, string)

                peggingPlayers.reverse()

            elif len(peggingPlayers) > 1:
                """
                A player calles go, because they can no longer play on the pile
                The opponent must continue to play while they can
                """
                peggingPlayers.pop(0)

            else:
                """
                Both players cannot play on the pile, but they still have cards
                The last player to play gets a go, unless they reached 31
                Then a new pile is started and pegging continues
                """
                if pile.sum() < 31:
                    peggingPlayers[0].addPoints(1, colored(" for the Go"))

                if players[0] == peggingPlayers[0]:
                    players.reverse()

                Cribbage.pegging(players)
                return

        if pile.sum() < 31:
            peggingPlayers[0].addPoints(1, colored(" for the Go"))



if __name__ == "__main__":
    Cribbage.playAIGame()
