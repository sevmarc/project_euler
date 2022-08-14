""" Number spiral diagonals
Starting with the number 1 and moving to the right in a clockwise 
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 
spiral formed in the same way?
"""
from math import pow


def recursive(x: int) -> int:
    """    0  1  2  (2n + 1)
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    """
    if x == 0:
        return 1
    sq = pow(2*x + 1, 2)
    return 4 * sq - 12 * x + recursive(x - 1)


if __name__ == '__main__':
    testing = False
    
    if testing:
        print(recursive(0))
        print(recursive(1))
        print(recursive(2))
        print(recursive(3))
    else:
        size_ = 1001
        n = (size_ - 1) / 2
        print(int(recursive(n)))
