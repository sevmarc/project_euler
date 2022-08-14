""" Non-abundant sums
A perfect number is a number for which the sum of its proper 
divisors is exactly equal to the number. For example, the sum 
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors 
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant 
numbers is 24. By mathematical analysis, it can be shown that all 
integers greater than 28123 can be written as the sum of two abundant 
numbers. However, this upper limit cannot be reduced any further 
by analysis even though it is known that the greatest number that 
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written 
as the sum of two abundant numbers.
"""

from function_collection.main import timer_wrapper
from function_collection.main import proper_divisors_fast


def deficient(x: int) -> bool:
    return x > sum(proper_divisors_fast(x))


def abundant(x: int) -> bool:
    return x < sum(proper_divisors_fast(x))


def perfect(x: int) -> bool:
    return x == sum(proper_divisors_fast(x))


def check_abundant_sum(x, ab: list[int]) -> bool:
    values = [i for i in ab if i < x]
    for v in values:
        if (x - v) in ab:
            # print(v, x-v)  # for actual results
            return True
    return False


def checker(ab: list[str]) -> int:
    return sum([i for i in range(1, limit) if not check_abundant_sum(i, ab)])


if __name__ == '__main__':
    testing = False

    limit = 28123
    abundants = [i for i in range(1, limit + 1) if abundant(i)]

    if testing:
        print(len(abundants))
        print(check_abundant_sum(24, abundants))
        print(check_abundant_sum(25, abundants))
        print(check_abundant_sum(23, abundants))
    else:
        print(timer_wrapper(checker, abundants))
