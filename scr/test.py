import cards as cds
from termcolor import colored
from cribbage import Cribbage
from termcolor import colored

def assertPoints(suits, ranks, isCrib, points):
    cards = []
    for i in range(len(suits)):
        cards.append(cds.Card(suits[i], ranks[i]))

    hand = cds.Deck(cards[:4])
    face = cds.Deck([cards[-1]])

    calculatedPoints, pointString = Cribbage.points(hand, face, isCrib)
    if calculatedPoints != points:
        print(pointString)
    assert calculatedPoints == points


def assertPegging(suits, ranks, points):
    cards = []
    for i in range(len(suits)):
        cards.append(cds.Card(suits[i], ranks[i]))

    pile = cds.Deck(cards)

    calculatedPoints = Cribbage.pointsPegging(pile)
    if calculatedPoints != points:
        print('points: ' + str(calculatedPoints))
    assert calculatedPoints == points

if __name__ == "__main__":

    # no points
    assertPoints(["♠","♥","♦","♣","♣"], [7,9,10,12,13], False, 0)

    # single pair
    assertPoints(["♠","♥","♦","♣","♣"], [9,9,10,12,13], False, 2)
    assertPoints(["♠","♥","♦","♣","♣"], [7,10,10,12,13], True, 2)
    assertPoints(["♠","♥","♦","♣","♦"], [7,9,10,13,13], False, 2)

    # two pair
    assertPoints(["♠","♥","♦","♣","♣"], [9,9,10,10,13], False, 4)
    assertPoints(["♠","♥","♦","♣","♣"], [1,1,12,12,13], True, 4)
    assertPoints(["♠","♥","♦","♣","♦"], [6,10,6,13,13], False, 4)

    # three of a kind
    assertPoints(["♠","♥","♦","♣","♣"], [9,9,9,12,13], False, 6)
    assertPoints(["♠","♥","♦","♣","♣"], [10,10,10,12,13], True, 6)
    assertPoints(["♠","♥","♦","♣","♦"], [1,1,1,10,13], False, 6)

    # full house
    assertPoints(["♠","♥","♦","♣","♣"], [9,9,9,13,13], False, 8)
    assertPoints(["♠","♥","♦","♣","♣"], [10,10,10,12,12], True, 8)
    assertPoints(["♠","♥","♦","♣","♦"], [1,1,1,10,10], False, 8)

    # four of a kind
    assertPoints(["♠","♥","♦","♣","♣"], [9,9,9,9,13], False, 12)
    assertPoints(["♠","♥","♦","♣","♣"], [10,10,10,10,13], True, 12)
    assertPoints(["♠","♥","♦","♣","♦"], [1,1,1,10,1], False, 12)

    # run, length 3
    assertPoints(["♠","♥","♦","♣","♣"], [13,12,11,1,2], False, 3)
    assertPoints(["♠","♥","♦","♣","♣"], [8,9,10,1,2], True, 3)
    assertPoints(["♠","♥","♦","♣","♣"], [10,1,11,2,12], False, 3)

    # run, length 4
    assertPoints(["♠","♥","♦","♣","♣"], [13,12,11,10,2], False, 4)
    assertPoints(["♠","♥","♦","♣","♦"], [8,9,10,11,2], True, 4)
    assertPoints(["♠","♥","♦","♣","♣"], [10,13,11,2,12], False, 4)

    # run, length 5
    assertPoints(["♠","♥","♦","♣","♣"], [13,12,11,10,9], False, 5)
    assertPoints(["♠","♥","♦","♣","♦"], [8,9,10,11,12], True, 5)
    assertPoints(["♠","♥","♦","♣","♣"], [10,13,11,9,12], False, 5)

    # double run, length 3
    assertPoints(["♠","♥","♦","♣","♣"], [13,12,11,12,2], False, 8)
    assertPoints(["♠","♥","♦","♣","♣"], [8,9,10,9,2], True, 8)
    assertPoints(["♠","♥","♦","♣","♥"], [10,1,11,11,12], False, 8)

    # double run, length 4
    assertPoints(["♠","♥","♦","♣","♣"], [13,12,11,12,10], False, 10)
    assertPoints(["♠","♥","♦","♣","♣"], [8,9,10,9,11], True, 10)
    assertPoints(["♠","♥","♦","♣","♥"], [10,13,11,11,12], False, 10)

    # tripple run, length 3
    assertPoints(["♠","♥","♦","♣","♠"], [13,12,11,12,12], False, 15)
    assertPoints(["♠","♥","♦","♣","♣"], [8,9,10,9,9], True, 15)
    assertPoints(["♠","♥","♦","♣","♠"], [10,11,11,11,12], False, 15)

    # knob
    assertPoints(["♠","♥","♦","♣","♦"], [7,9,11,1,13], False, 1)
    assertPoints(["♠","♥","♦","♣","♦"], [2,9,11,1,13], True, 1)

    # Best Possible hand
    assertPoints(["♠","♥","♦","♣","♣"], [5,5,5,11,5], False, 29)
    assertPoints(["♠","♥","♦","♣","♣"], [5,5,5,11,5], True, 29)


    # Zero point piles
    assertPegging(["♠"], [5], 0)
    assertPegging(["♥"], [13], 0)
    assertPegging(["♦"], [1], 0)
    assertPegging(["♣"], [9], 0)

    assertPegging(["♣","♣","♣","♣"], [9,4,7,1], 0)
    assertPegging(["♠","♥","♦","♣","♣"], [1,2,4,5,13], 0)
    assertPegging(["♣","♥"], [9, 8], 0)

    # Pair piles
    assertPegging(["♣","♥"], [1,1], 2)
    assertPegging(["♠","♥","♦","♣","♦"], [1,2,4,13,13], 2)

    # Pervious pairs (0 points)
    assertPegging(["♣","♥","♣","♣"], [9,9,7,1], 0)
    assertPegging(["♠","♥","♦","♣","♦","♦"], [1,2,4,13,13,2], 0)

    # Three of a kind piles
    assertPegging(["♣","♥","♦"], [1,1,1], 6)
    assertPegging(["♠","♥","♦","♣","♦","♥"], [1,2,4,7,7,7], 6)

    # Three of a kind piles (0 points)
    assertPegging(["♣","♥","♦","♦"], [1,1,1,2], 0)
    assertPegging(["♠","♥","♦","♣","♦","♥","♥"], [1,2,4,7,7,7,1], 0)

    # Four of a kind piles
    assertPegging(["♣","♥","♦","♠"], [1,1,1,1], 12)

    # Four of a kind piles (0 points)
    assertPegging(["♣","♥","♦","♠","♠"], [1,1,1,1,2], 0)

    # Run pile, length 3
    assertPegging(["♠","♥","♦"], [11,12,13], 3)
    assertPegging(["♠","♥","♦"], [8,10,9], 3)
    assertPegging(["♠","♥","♦","♣","♣"], [1,1,7,8,6], 3)

    # Run pile, length 3, (0 points)
    assertPegging(["♠","♥","♦","♦"], [9,10,11,1], 0)
    assertPegging(["♠","♥","♦","♦"], [8,10,9,2], 0)

    # Run pile, length 4
    assertPegging(["♠","♥","♦","♦"], [1,2,3,4], 4)
    assertPegging(["♠","♥","♦","♦"], [7,6,5,8], 4)
    assertPegging(["♠","♥","♦","♣","♣"], [1,1,2,3,4], 4)

    # Run pile, length 7
    assertPegging(["♠","♥","♦","♦","♦","♦","♦"], [1,2,3,4,5,6,7], 7)
    assertPegging(["♠","♥","♦","♦","♦","♦","♦"], [5,2,7,4,1,6,3], 7)

    # Fifteen pile
    assertPegging(["♠","♥"], [10,5], 2)
    assertPegging(["♠","♥","♦","♦"], [1,4,6,4], 2)

    # Fifteen and Pairs
    assertPegging(["♠","♥","♥","♦"], [1,4,5,5], 4)
    assertPegging(["♠","♠","♥","♦","♣"], [7,2,2,2,2], 14)

    # Fifteen and runs
    assertPegging(["♥","♦","♣"], [4,5,6], 5)
    assertPegging(["♠","♥","♦","♣","♠"], [2,4,1,3,5], 7)

    # Thirty-one pile
    assertPegging(["♠","♥","♦","♦"], [10,10,10,1], 2)
    assertPegging(["♠","♥","♦","♣","♠","♥","♦","♣","♠","♥","♦","♣","♣"], [1,1,1,1,2,2,2,2,3,3,3,4,6], 2)

    # Thirty-one pile and pairs
    assertPegging(["♠","♥","♦","♦","♥"], [10,10,9,1,1], 4)
    assertPegging(["♠","♥","♠","♥","♦","♣"], [10,5,4,4,4,4], 14)

    # Thirty-one pile and runs
    assertPegging(["♠","♥","♦","♣"], [1,10,12,11], 5)
    assertPegging(["♠","♥","♦","♣","♠","♥","♦","♣"], [3,7,1,2,3,6,5,4], 9)


    print(colored("All tests Passed", 'white', 'on_green'))
