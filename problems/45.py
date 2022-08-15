""" Triangular, pentagonal, and hexagonal
Triangle, pentagonal, and hexagonal numbers are generated 
by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n-1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

from function_collection.main import timer_wrapper

l = 100000


def triangle(limit: int = l) -> list[int]:
    return [int(i * (i + 1) / 2) for i in range(1, limit)]


def pentagonal(limit: int = l) -> list[int]:
    return [int(i * (3 * i - 1) / 2) for i in range(1, limit)]


def hexagonal(limit: int = l) -> list[int]:
    return [int(i * (2 * i - 1)) for i in range(1, limit)]


def calc45() -> int:
    tri_ = triangle()
    pen_ = pentagonal()
    hex_ = hexagonal()

    return [tn for tn in tri_ if tn in pen_ and tn in hex_][2]


if __name__ == '__main__':
    result = timer_wrapper(calc45)
    print(f"{result = }")
