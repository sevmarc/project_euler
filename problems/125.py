""" Palindromic sums
The palindromic number 595 is interesting because it can be written 
as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 
122.

There are exactly eleven palindromes below one-thousand that can be 
written as consecutive square sums, and the sum of these palindromes 
is 4164. 
Note that 1 = 02 + 12 has not been included as this problem is 
concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both 
palindromic and can be written as the sum of consecutive squares.
"""

from function_collection.main import timer_wrapper, is_palindrome, is_square
from math import sqrt


def consecutive_squairs_from_start(start: int, goal: int) -> bool:
    conseqs = [start**2]
    steps = 0
    while (goal > sum(conseqs)):
        steps += 1
        conseqs.append((start + steps)**2)
    if sum(conseqs) == goal:
        return True
    else:
        return False


def sum_of_consequtive_squairs(x: int) -> bool:
    if (0 > x) or is_square(x):
        return False
    starter = 1
    while (starter < (sqrt(x) - 1)):
        if consecutive_squairs_from_start(starter, x):
            return True
        starter += 1
    return False


def calc125(limit_: int = 100000000) -> int:
    return sum([1 for i in range(limit_) if sum_of_consequtive_squairs(i) and is_palindrome(i)])


if __name__ == '__main__':
    testing = False

    if testing:
        print(sum_of_consequtive_squairs(595))
        print(sum_of_consequtive_squairs(596))
    else:
        print(timer_wrapper(calc125))
