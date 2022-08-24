""" Totient permutation
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal 
to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, 
and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive 
number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a 
permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n 
and the ratio n/φ(n) produces a minimum.
"""

from collections import Counter
from function_collection.main import proper_divisors_fast
from function_collection.main import unique_prime_divisors
from function_collection.main import timer_wrapper


def compare_permutation(arg1: int, arg2: int) -> bool:
    return Counter(str(arg1)) == Counter(str(arg2))


def phi(n: int) -> int:
    return n - sum([(int(n/i) - 1) for i in unique_prime_divisors(n)]) - 1


def calc70() -> int:
    n = 10000000
    min_ = 1000

    for i in range(2, n):
        f = phi(i)
        if compare_permutation(i, f) and float(i / f) < min_:
            min_ = float(i / f)
            place = i
    return place


if __name__ == '__main__':
    testing = True

    if testing:
        print(f"{proper_divisors_fast(125) = }")
        print(f"{proper_divisors_fast(625) = }")
        print(f"125: {unique_prime_divisors(125) = }")
        print(f"25: {unique_prime_divisors(25) = }")
        print(f"5: {unique_prime_divisors(5) = }")

        print(f"{phi(9) = }")
        print(f"{phi(87109) = }")
    else:
        result = timer_wrapper(calc70)  # ~100 sec
        print(f"{result = }")
