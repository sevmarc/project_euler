""" Sub-string divisibility
The number, 1406357289, is a 0 to 9 pandigital number because 
it is made up of each of the digits 0 to 9 in some order, but 
it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. 
In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from collections import Counter
from itertools import permutations
from function_collection.main import timer_wrapper

digits = "0123456789"
explen = 10


def pandigital(w: str) -> bool:
    if len(w) != 10:
        return False
    for i, j in Counter(w).items():
        if j != 1 or i not in digits:
            return False
    return True


def cond(w: str, d1: int, d2: int, d3: int, div: int) -> int:
    return int(w[d1 - 1] + w[d2 - 1] + w[d3 - 1]) % div == 0


def cond1(w: str) -> int:
    return cond(w, 2, 3, 4, 2)


def cond2(w: str) -> int:
    return cond(w, 3, 4, 5, 3)


def cond3(w: str) -> int:
    return cond(w, 4, 5, 6, 5)


def cond4(w: str) -> int:
    return cond(w, 5, 6, 7, 7)


def cond5(w: str) -> int:
    return cond(w, 6, 7, 8, 11)


def cond6(w: str) -> int:
    return cond(w, 7, 8, 9, 13)


def cond7(w: str) -> int:
    return cond(w, 8, 9, 10, 17)


def calc43() -> int:
    result = sum([int(''.join(j)) for j in list(permutations(digits)) if pandigital(j) and cond1(
        j) and cond2(j) and cond3(j) and cond4(j) and cond5(j) and cond6(j) and cond7(j)])
    return result


if __name__ == '__main__':
    testing = False

    if testing:
        print(pandigital("1406357289"))
        print(pandigital("1403257869"))
        print(pandigital("14063249"))
        print(pandigital("1234"))
    else:
        print(timer_wrapper(calc43))
