import cards as cds

class Cribbage():
    def points(hand, face, isCrib=False, ):
        cards = hand + face
        cards.sort()
        points = 0
        string = ""

        nPoints, nString = Cribbage.fifteens(cards)
        points += nPoints
        string += nString

        nPoints, nString = Cribbage.pairs(cards)
        points += nPoints
        string += nString

        nPoints, nString = Cribbage.runs(cards)
        points += nPoints
        string += nString

        nPoints, nString = Cribbage.flush(hand, face, isCrib)
        points += nPoints
        string += nString

        nPoints, nString = Cribbage.nob(hand,face)
        points += nPoints
        string += nString

        return points, string


    def fifteens(cards):
        points = 0
        string = ""
        for combo in cards.combinations():
            if combo.sum() == 15:
                points += 2
                string += "15: " + str(combo) + "\n"
        return points, string


    def pairs(cards):
        points = 0
        string = ""
        for combo in cards.combinations(2):
            if combo.cards[0].rank == combo.cards[1].rank:
                points += 2
                string += "pair: " + str(combo) + "\n"
        return points, string


    def runs(cards):
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
        points = 0
        string = ""
        for card in hand.cards:
            if card.rank == 11 and card.suit == face.cards[0].suit:
                points = 1
                string = "nob with the " + str(card) + "\n"
        return points, string


if __name__ == "__main__":
    deck = cds.Deck()
    deck.shuffle()
    suits = cds.Card.suits()

    hand = cds.Deck([cds.Card(suits[0],1), cds.Card(suits[1],1), cds.Card(suits[0],2), cds.Card(suits[0],3)])
    face = deck.draw()

    print("hand: " + str(hand))
    print("face: " + str(face))
    print("\n")
    Cribbage.points(hand, face)
