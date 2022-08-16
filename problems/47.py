""" Distinct primes factors
The first two consecutive numbers to have two distinct 
prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct 
prime factors are:

644 = 2² x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct 
prime factors each. What is the first of these numbers?
"""

from function_collection.main import is_prime
from function_collection.main import timer_wrapper


def primes(n: int, lista: list = []) -> list[int]:
    if not lista:
        result = []
        if is_prime(n):
            result.append(n)
            return result
    else:
        result = lista
    for i in range(2, n):
        if (n % i) == 0:
            result.append(i)
            n = int(n / i)
            if is_prime(n):
                result.append(n)
                return result
            primes(n, result)
            break
    return result


def prime_dict(n: int) -> int:
    l = primes(n)
    pd = {p: l.count(p) for p in set(l)}
    return len(set(sorted(pd)))


def calc47() -> int:
    lookfor = 4
    current = i = 0
    found = False

    while not found:
        if prime_dict(i) >= lookfor:
            current += 1
        else:
            current = 0
        if current == lookfor:
            found = True
            return i - 3
        i += 1

if __name__ == '__main__':
    result = timer_wrapper(calc47)
    print(f"{result = }")
