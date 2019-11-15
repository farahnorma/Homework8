

import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

# here's two Python classes whose objects represent playing cards and decks thereof

class Card():
    """
    Represents a single playing card,
        whose rank internally is int _rank: 1..13 => "Ace".."King"
        and whose suit internally is int _suit 0..3 => "Clubs".."Spades"
    """

    def __init__(self, rank=1, suit=3): # this is the constructor!
        '''
        Initialize card with given int suit and int rank
        :param rank:
        :param suit:
        :return:
        '''
        self._rank = rank
        self._suit = suit

    def __str__(self): # this is the "stringifier"
        """
        Return the string name of this card:
        "Ace of Spades": translates int fields to strings
        :return:
        """

        # "Ace of Spades" is string for self._rank==1, self._suit==3

        toreturn = RANKS[self._rank] + " of " + SUITS[self._suit]

        return toreturn


class Deck():
    """
    Represents a deck of 52 standard playing cards,
        as a list of Card refs
    """

    def __init__(self): # constructor
        """
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        :return: nothing
        """

        self._cards = []
        for rank in range(1, 14):
            for suit in range(4):
                c = Card(rank, suit) # create next Card with given value
                self._cards.append(c) # add it to this Deck

    def __str__(self):
        """
        "Stringified" deck: string of Card named,
        with \n for easier reading
        :return:
        """
        toreturn = ''

        # for index in range(len(self._cards)):
        #     self._cards[index]

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            toreturn = toreturn + temp + "\n"  # note \n at end

        return toreturn

    def shuffle(self):
        random.shuffle(self._cards)  # note random function to do this

    def dealCard(self):
        toreturn = self._cards.pop(0)  # get and remove top card from deck
        return toreturn

def buildDict(hand):
    dict = {}

    for card in hand:
        dict[card._rank] = dict.get(card._rank, 0) + 1

    # for card in hand:
    #     dict[card._suit] = dict.get(card._suit, 0) + 1
    # Complete this

    return dict


def hasOnePair(dict):
    # Check for EXACTLY one pair in dict and no three-of-a-kinds
    twocount = 0
    threecount = 0
    for v in dict.values():
        if v == 2:
            twocount += 1
        elif v == 3:
            threecount += 1

    if twocount==1 and threecount != 1:
        return True
    else:
        return False

    return twocount==1 and threecount!=1
    # return False  # fix this...


def hasTwoPairs(dict):
    twocount = 0

    for v in dict.values():
        if v == 2:
            twocount += 1


    return twocount ==2




def hasThreeOfAKind(dict):
    twocount = 0
    threecount = 0
    for v in dict.values():
        if v == 2:
            twocount += 1
        if v == 3:
            threecount += 1

    return threecount is 1 and twocount is not 1   # exactly  1 3 of a kind and no pairs

def hasFullHouse(dict):
    twocount = 0
    threecount = 0
    for v in dict.values():
        if v == 2:
            twocount += 1
        if v == 3:
            threecount += 1

        return twocount is 1 and threecount is 1  # exactly 1 pair and 1 3 of a kind


def hasFourOfAKind(dict):

    fourcount = 0
    for v in dict.values():
        if v == 4:
            fourcount += 1

    return fourcount is 1

def hasStraight(dict):
    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False

def hasFlush(dict):
    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False

def hasStraightFlush(dict):
    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False

def hasRoyalFlush(dict):
    """
    Complete this!
    :param dict: dictionary with card ranks to check
    """

    return False

def main():

    # finish this...

    TRIALS = 100000  # int(input ("Input number of hands to test: "))

    hand = []  # list of Card in hand

    # accumulators for different counts

    onepairCount = 0
    twopairCount = 0
    threeCount = 0
    fourCount = 0
    fullHouseCount = 0

    # more if you wish...

    for num in range(TRIALS):

        # create new Deck and shuffle
        d = Deck()
        d.shuffle()

        # initialize hand as empty list
        hand = []

        # deal top 5 cards of deck, adding to hand

        for count in range(5):
            hand.append(d.dealCard())

        # build the dictionary of card ranks in hand

        dict = buildDict(hand)

        # use dictionary to make hand checking easier

        if hasOnePair(dict):
            onepairCount += 1
        elif hasTwoPairs(dict):
            twopairCount += 1
        elif hasThreeOfAKind(dict):
            threeCount += 1
        elif hasFourOfAKind(dict):
            fourCount += 1
        elif hasFullHouse(dict):
            fullHouseCount += 1


    print("Number of one pair hands is: ", onepairCount)
    print("% of hands: ", 100.0 * onepairCount / TRIALS)

    print("Number of two pair hands is: ", twopairCount)
    print("% of hands: ", 100.0 * twopairCount / TRIALS)

    print("Number of three of a kind hands is: ", threeCount)
    print("% of hands: ", 100.0 * threeCount / TRIALS)

    print("Number of four of a kind hands is: ", fourCount)
    print("% of hands: ", 100.0 * fourCount / TRIALS)

    print("Number of full house hands is: ", fullHouseCount)
    print("% of hands: ", 100.0 * fullHouseCount / TRIALS)


def card_example():

    card1 = Card()  # Card(1,3) => Ace of Clubs
    card2 = Card(12, 2) # Card (12,2) => Queen of Hearts

    card1._newfield = 47 # we can add new fields to any Python object!

    # three ways of printing a Card
    #

    print(card1.__str__())  # calling the methods against card
    print(str(card2)) # type-casting
    print(card2) # short-cut: passing obj ref to print does str() automagically

    print(card1._newfield) # see the new field value?

    print(card1._rank) # see the rank (1..13)
    print(card1._suit) # see the suit (0..3)

def deck_example():
    """
    Test Deck: create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    """

    deck = Deck()
    print(str(deck)) # see entire deck before shuffling

    print("Now we shuffle:\n")

    deck.shuffle()
    print(str(deck)) # see entire deck after shuffling

    card1 = deck.dealCard()
    card2 = deck.dealCard()

    print("The first card dealt is", str(card1), "and the second is", str(card2))
    print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!

if __name__ == "__main__": # only run this if this .py is NOT imported
    pass

    # card_example() # uncomment to test creating & calling Card methods

    #deck_example()  # uncomment to test Deck: create, print, shuffle, print

    main()  # uncomment to run general poker odds calculations

#
# -------------------------------------------------------------------------
#

# a sample pytest follows...

def test_one_pair1():
    testhand = [Card(2, 3), Card(1, 2),
                Card(3, 3), Card(7, 2),
                Card(2, 0)]

    dict = buildDict(testhand)

    assert hasOnePair(dict)

def test_one_pair2():
    testhand = [Card(3, 3), Card(1, 2),
                Card(3, 1), Card(13, 2),
                Card(2, 1)]

    dict = buildDict(testhand)

    assert hasOnePair(dict)

def test_one_pair3():
    testhand = [Card(2, 3), Card(13, 1),
                Card(5, 1), Card(13, 2),
                Card(4, 0)]

    dict = buildDict(testhand)

    assert hasOnePair(dict)


def test_two_pair1():
    testhand = [Card(2, 3), Card(3, 2),
                Card(3, 3), Card(7, 2),
                Card(2, 0)]

    dict = buildDict(testhand)

    assert hasTwoPairs(dict)


def test_two_pair2():
    testhand = [Card(4, 3), Card(1, 2),
                Card(5, 1), Card(4, 2),
                Card(5, 2)]

    dict = buildDict(testhand)

    assert hasTwoPairs(dict)


def test_two_pair3():
    testhand = [Card(2, 3), Card(13, 1),
                Card(5, 1), Card(13, 2),
                Card(5, 0)]

    dict = buildDict(testhand)

    assert hasTwoPairs(dict)



def test_three1():
    testhand = [Card(2, 3), Card(3, 2),
                Card(2, 1), Card(7, 2),
                Card(2, 0)]

    dict = buildDict(testhand)

    assert hasThreeOfAKind(dict)


def test_three2():
    testhand = [Card(5, 3), Card(1, 2),
                Card(5, 1), Card(4, 2),
                Card(5, 2)]

    dict = buildDict(testhand)

    assert hasThreeOfAKind(dict)


def test_three3():
    testhand = [Card(2, 3), Card(13, 1),
                Card(5, 1), Card(13, 2),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasThreeOfAKind(dict)


def test_four1():
    testhand = [Card(2, 3), Card(2, 2),
                Card(2, 1), Card(7, 2),
                Card(2, 0)]

    dict = buildDict(testhand)

    assert hasFourOfAKind(dict)


def test_four2():
    testhand = [Card(5, 3), Card(5, 0),
                Card(5, 1), Card(4, 2),
                Card(5, 2)]

    dict = buildDict(testhand)

    assert hasFourOfAKind(dict)


def test_four3():
    testhand = [Card(13, 3), Card(13, 1),
                Card(5, 1), Card(13, 2),
                Card(13, 0)]

    dict = buildDict(testhand)

    assert hasFourOfAKind(dict)

def test_fullhouse1():
    testhand = [Card(2, 3), Card(3, 2),
                Card(3, 3), Card(3, 1),
                Card(2, 0)]

    dict = buildDict(testhand)

    assert hasFullHouse(dict)


def test_fullhouse2():
    testhand = [Card(4, 3), Card(4, 0),
                Card(5, 1), Card(4, 2),
                Card(5, 2)]

    dict = buildDict(testhand)

    assert hasFullHouse(dict)


def test_fullhouse3():
    testhand = [Card(5, 3), Card(13, 1),
                Card(5, 1), Card(13, 2),
                Card(5, 0)]

    dict = buildDict(testhand)

    assert hasFullHouse(dict)
main()