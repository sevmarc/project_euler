""" Prime permutations
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: (i) each of the three terms 
are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from function_collection.main import is_prime
from function_collection.main import timer_wrapper
from itertools import permutations


def cond1(x1: int, x2: int, x3: int) -> bool:
    return is_prime(x1) and is_prime(x2) and is_prime(x3)


def word_permutations(x: int) -> list[str]:
    return [''.join([l for l in w]) for w in list(permutations(str(x)))]


def calc49() -> int:
    found = 0
    jump = 3330
    for i in range(1000, 3400):
        j1 = i + jump
        j2 = i + 2 * jump
        if cond1(i, j1, j2) and str(j1) in word_permutations(i) and str(j2) in word_permutations(i):
            found += 1
            if found == 2:
                return int(str(i) + str(j1) + str(j2))

if __name__ == '__main__':
    result = timer_wrapper(calc49)
    print(f"{result = }")
