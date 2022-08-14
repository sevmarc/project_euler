""" Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from function_collection.main import is_prime, timer_wrapper


def calc10(max_: int) -> int:
    return sum([i for i in range(1, max_ + 1) if is_prime(i)])


if __name__ == '__main__':
    print(timer_wrapper(calc10, 2000000))
