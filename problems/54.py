""" Poker hands
In the card game poker, a hand consists of five cards and 
are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made 
up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). 
But if two ranks tie, 
for example, both players have a pair of queens, then highest cards in 
each hand are compared (see example 4 below); 
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD   2C 3S 8S 8D TD     Player 2
        Pair of Fives    Pair of Eights
2	 	5D 8C 9S JS AC    2C 5C 7D 8S QH    Player 1
       Highest card Ace  Highest card Queen
3	 	2D 9C AS AH AC   3D 6D 7D TD QD     Player 2
          Three Aces     Flush with Diamonds
4	 	4D 6S 9H QH QC   3D 6D 7H QD QS     Player 1
        Pair of Queens    Pair of Queens
      Highest card Nine  Highest card Seven
5	 	2H 2D 4C 4D 4S    3C 3D 3S 9S 9D    Player 1
         Full House        Full House
       With Three Fours  with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

from typing import Collection
from function_collection.main import timer_wrapper
from collections import Counter, OrderedDict


def get_rank(cardnum: str) -> int:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    try:
        return ranks.index(cardnum)
    except ValueError:  # value not in self.ranks list, incorrect input
        return -1

class Card:
    def __init__(self, data: str):
        self.value = data[0]  # 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
        self.color = data[1]  # H, S, D, C
        self.symbol: str = str(self.value) + str(self.color)
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    def get_rank(self) -> int:
        return get_rank(self.value)

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.values = [card.get_rank() for card in cards]
        self.highest_value = list(reversed(sorted(self.values)))
        self.value_counter = Counter(self.values)

        self.colors = [card.color for card in cards]
        self.color_counter = Counter(self.colors)
        # primary rank, secondary rank to settle ties
        self.rank = []
        self.evaluate_value()

    def evaluate_value(self):
        """
        High Card: Highest value card.
        One Pair: Two cards of the same value.
        Two Pairs: Two different pairs.
        Three of a Kind: Three cards of the same value.
        Straight: All cards are consecutive values.
        Flush: All cards of the same suit.
        Full House: Three of a kind and a pair.
        Four of a Kind: Four cards of the same value.
        Straight Flush: All cards are consecutive values of same suit.
        Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        """
        
        self.ranklist = [
            self.high_card,
            self.pairs,
            self.three_of_a_kind,
            self.straight,
            self.flush,
            self.full_house,
            self.four_of_a_kind,
            self.straight_flush,
            self.royal_flush
        ]

        for card_pattern in reversed(self.ranklist):
            if card_pattern():
                # print('Pattern: ', self, self.rank)
                break
        
    def high_card(self) -> bool:
        # high card
        self.rank = [0, max(self.values)]
        return True

    def pairs(self) -> bool:
        # one pair, two pairs
        if 2 in self.value_counter.values():
            pairs = max_c = 0
            for c in self.value_counter:
                if self.value_counter[c] == 2:
                    if c > max_c:
                        max_c = c
                    pairs += 1
            if pairs == 1:
                self.rank = [1, max_c]
            if pairs == 2:
                self.rank = [2, max_c]
            return True
        else:
            return False

    def three_of_a_kind(self) -> bool:
        # three of a kind
        if 3 in self.value_counter.values():
            for c in self.value_counter:
                if self.value_counter[c] == 3: 
                    find_triple_value = c
            self.rank = [3, find_triple_value]
            return True
        else:
            return False

    def straight(self) -> bool:
        # straight
        pre_ = starter_value = sorted(self.values)[0] - 1  # to 
        straight = True
        for v in sorted(self.values):
            if v - pre_ != 1:
                straight = False
            pre_ = v
        if straight:
            self.rank = [4, starter_value]
            return True
        else:
            return False

    def flush(self) -> bool:
        # flush
        if len(self.color_counter) == 1:  # all color is the same
            self.rank = [5, 0]  # no secondary rank
            return True
        else:
            return False

    def full_house(self) -> bool:
        if 3 in self.value_counter.values() and \
           2 in self.value_counter.values():
            for c in self.value_counter:
                if self.value_counter[c] == 3:
                    find_triple_value = c
            self.rank = [6, find_triple_value]
            return True
        else:
            return False

    def four_of_a_kind(self):
        if 4 in self.value_counter.values():
            for c in self.value_counter:
                if self.value_counter[c] == 4:
                    kind = c
            self.rank = [7, kind]
            return True
        else:
            return False

    def straight_flush(self):
        if len(self.color_counter) == 1:  # same color
            pre_ = starter_value = sorted(self.values)[0] - 1
            straight = True
            for v in sorted(self.values):
                if v - pre_ != 1:
                    straight = False
                pre_ = v
            if straight:
                self.rank = [8, starter_value]
                return True
            else:
                return False

    def royal_flush(self):
        pattern = [10, 11, 12, 13, 14]
        if sorted(self.values) == pattern and len(self.color_counter) == 1:
            self.rank = [9, 0]
            return True
        else:
            return False

    def __str__(self):
        """ Builtin used when print() is called on an instance """
        repr_ = ''
        for c in self.cards:
            repr_ += c.symbol + ' '
        return repr_
    
    def __repr__(self):
        return self.__str__()


def compete_hands(hand1: Hand, hand2: Hand) -> bool:
    """
    Battle of 2 pairs, returns True if hand1 wins
    """
    if hand1.rank[0] == hand2.rank[0]:  # same type
        if hand1.rank[1] == hand2.rank[1]:
            # checking highest different card
            for i in range(5):
                if hand1.highest_value[i] == hand2.highest_value[i]:
                    continue
                elif hand1.highest_value[i] > hand2.highest_value[i]:
                    return True
                else:
                    return False
        if hand1.rank[1] > hand2.rank[1]:
            return True
        else:
            return False
    elif hand1.rank[0] > hand2.rank[0]:
        return True
    else:
        return False


def read_hands(poker_file: str, printer: bool=False) -> list[tuple[Hand]]:
    hands = []
    with open(poker_file) as pf:
        lines = pf.readlines()
        for l in lines:
            cards = l.split(' ')
            cards_in_first_hand = [Card(c) for c in cards[:5]]
            cards_in_second_hand = [Card(c) for c in cards[5:]]
            hands.append( (Hand(cards_in_first_hand), Hand(cards_in_second_hand)) )
    if printer:
        for i in hands:
            print(i)
    return hands

def play_tournament(hand_pairs: list[list[Hand]]) -> int:
    result = 0
    for hand_pair in hand_pairs:
        if compete_hands(hand_pair[0], hand_pair[1]):
            result += 1
    return result


if __name__ == '__main__':
    hand_pairs = read_hands('inputfiles/54_poker.txt')
    print(play_tournament(hand_pairs))
