""" Powerful digit sum
A googol (10^100) is a massive number: one followed by 
one-hundred zeros; 100^100 is almost unimaginably large: one 
followed by two-hundred zeros. Despite their size, the sum of 
the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, 
what is the maximum digital sum?
"""

from function_collection.main import timer_wrapper
from math import pow


def calc_digits(x: int) -> int:
    return sum([int(w) for w in str(x)])


def iter(limit_a: int, limit_b: int) -> int:
    result_list = [calc_digits(int(pow(i, j)))
                   for i in range(limit_a) for j in range(limit_b)]
    return max(result_list)


if __name__ == '__main__':
    # should be 972, too large number cause some trouble
    print(timer_wrapper(iter, [100, 100]))
