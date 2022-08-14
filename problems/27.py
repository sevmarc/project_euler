""" Quadratic primes
https://projecteuler.net/problem=27
"""
from math import sqrt
from function_collection.main import is_prime


def equa(x: int, a: int, b: int) -> bool:
    cur = x*x + a*x + b
    return is_prime(cur)


def quad(a: int, b: int) -> int:
    x = 0
    while (equa(x, a, b)):
        x += 1
    return x


if __name__ == '__main__':
    testing = False

    if testing:
        print(quad(-79, 1601))
    else:
        constr = 1000
        max_ = max_a = max_b = 0

        for a in range(-constr, constr):
            for b in range(-constr, constr):
                cur = quad(a, b)
                if cur > max_:
                    max_ = cur
                    max_a = a
                    max_b = b
        print(f"{max_a = }, {max_b = }: {max_}")
        print(f"Result: {max_a*max_b}")
