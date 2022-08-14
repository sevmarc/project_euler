""" Circular primes
The number, 197, is called a circular prime because all 
rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from function_collection.main import is_prime


def circulate(x: int) -> list[int]:
    w = str(x)
    return [int(w[i:] + w[:i]) for i in range(len(w))]


def check_circular_if_prime(l: list[int]) -> bool:
    for i in l:
        if not is_prime(i):
            return False
    return True


def calc35(maxval: int = 1000000) -> int:
    return len(list(filter(None, [check_circular_if_prime(circulate(i)) for i in range(2, maxval)])))


if __name__ == '__main__':
    testing = False

    if testing:
        print(circulate(197))
        print(circulate(1234))
    else:
        result = calc35()
        print(f"{result = }")
