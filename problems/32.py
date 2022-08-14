""" Pandigital products
We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once; for example, the 5-digit 
number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure 
to only include it once in your sum.
"""

from collections import Counter
from function_collection.main import timer_wrapper


digits = '123456789'


def pandigital(x: int) -> bool:
    return Counter(str(x)) == Counter(digits[:len(str(x))])


def pandigital_n(x: int, n: int) -> bool:
    if len(str(x)) != n:
        return False
    return Counter(str(x)) == Counter(digits[:len(str(x))])


def checker() -> int:
    limit_p1 = 10000
    limit_p2 = 10000
    result = [i*j for i in range(limit_p1) for j in range(limit_p2)
              if pandigital_n(int(str(i) + str(j) + str(i * j)), 9)]
    return sum(set(result))


if __name__ == '__main__':
    testing = False

    if testing:
        print(pandigital(5))
        print(pandigital_n(1234, 4))
        print(pandigital_n(1234, 3))
        print(pandigital(1))
        print(pandigital(23456))
    else:
        print(timer_wrapper(checker))
