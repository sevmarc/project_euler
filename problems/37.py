""" Truncatable primes
The number 3797 has an interesting property. Being prime 
itself, it is possible to continuously remove digits from left 
to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from function_collection.main import is_prime
from function_collection.main import timer_wrapper


def trunc_left(x: int) -> bool:
    w = str(x)
    if len(w) > 1:
        return is_prime(x) and trunc_left(int(w[1:]))
    else:
        return is_prime(x)


def trunc_right(x: int) -> bool:
    w = str(x)
    if len(w) > 1:
        return is_prime(x) and trunc_right(int(w[:len(w)-1]))
    else:
        return is_prime(x)


def calc37(maxval: int = 1000000) -> int:
    result_list = [i for i in range(
        10, maxval) if trunc_left(i) and trunc_right(i)]
    return sum(result_list)


if __name__ == '__main__':
    testing = False

    if testing:
        print(trunc_left(3797))
        print(trunc_right(3797))
        print(trunc_left(7))
    else:
        result = timer_wrapper(calc37)
        print(f"{result = }")
