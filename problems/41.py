""" Pandigital prime
We shall say that an n-digit number is pandigital if it 
makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
from function_collection.main import is_prime

digits = "123456789"


def scramble(x: str) -> list[tuple[str]]:
    return list(permutations(x))


def calc41() -> int:
    max_ = 0
    for i in range(1, len(digits) + 1):
        for s in scramble(digits[:i]):
            u = "". join([l for l in s])
            if is_prime(int(u)) and int(u) > max_:
                max_ = int(u)
    return max_


if __name__ == '__main__':
    print(calc41())
