""" Counting fractions
Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in 
ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 
3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper 
fractions for d ≤ 1,000,000?
"""

from function_collection.main import unique_prime_divisors, timer_wrapper
from math import gcd as bltin_gcd
from sympy import totient


def hcf_1(d: int) -> int:
    """ Returns the number of numbers that have a HCF 
    of 1 with the input 'd' number """
    return len([i for i in range(1, d) if bltin_gcd(i, d) == 1])


def calc_rec(lim_: int) -> int:
    """ Sums hcf_1s recursively """
    if lim_ == 1:
        return 0
    return hcf_1(lim_) + calc_rec(lim_-1)


def calc_lin(lim_: int) -> int:
    """ Sums hcf_1s linearly """
    return sum([hcf_1(i) for i in range(lim_ + 1)])


def calc_tot(lim_: int) -> int:
    """ Sums hcf_1s using Euler's totient function (from sympy) """
    return sum([totient(i) for i in range(2, lim_ + 1)])


if __name__ == '__main__':
    testing = False
    if testing:
        for i in range(2, 26):
            print(i, hcf_1(i))
    else:
        val = int(1e6)
        print(timer_wrapper(calc_tot, val))
