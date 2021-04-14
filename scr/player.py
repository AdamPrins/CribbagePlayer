import cribbage as crib
import cards as cds

class Player():
    def __init__(self):
        points = 0
        hand = None

    def deal(self, cards):
        if len(cards) != 6:
            raise ValueError("hand must be six cards")

        remaining = cds.Deck() - cards


        hands = []
        for hand in cards.combinations(4):
            handValue = {
                "hand": hand,
                "pointsSum": 0,
                "points": []
            }

            for card in remaining.combinations(1):
                points, _ =crib.Cribbage.points(hand, card, False)
                handValue["pointsSum"]+=points
                handValue["points"].append(points)
            hands.append(handValue)

        seq = [hand['pointsSum'] for hand in hands]
        best = seq.index(max(seq))

        print(hands[best])


if __name__ == "__main__":
    deck = cds.Deck()
    player1 = Player()

    player1.deal(deck.draw(6))
