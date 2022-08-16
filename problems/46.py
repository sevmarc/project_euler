""" Goldbach's other conjecture
It was proposed by Christian Goldbach that every odd 
composite number can be written as the sum of a prime 
and twice a square.

9 = 7 + 2x12
15 = 7 + 2x22
21 = 3 + 2x32
25 = 7 + 2x32
27 = 19 + 2x22
33 = 31 + 2x12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be 
written as the sum of a prime and twice a square?
"""

from math import sqrt
from function_collection.main import is_prime
from function_collection.main import timer_wrapper


def check_goldbach(x: int) -> bool:
    return any([i for i in range(x) if is_prime(i) and sqrt((x - i) / 2).is_integer()])


def calc46() -> int:
    found = False
    i = 1

    while not found:
        i += 1
        cur = 2 * i - 1
        if not is_prime(cur) and not check_goldbach(cur):
            found = True
    return cur


if __name__ == '__main__':
    result = timer_wrapper(calc46)
    print(f"{result = }")
