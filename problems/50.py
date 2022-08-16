""" Consecutive prime sum
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime 
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds 
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the 
most consecutive primes?
"""

from function_collection.main import is_prime, generate_primes
from function_collection.main import timer_wrapper


def sum_in_range(lst: list[int], start: int, finish: int) -> int:
    return sum([lst[i] for i in range(start, finish)])


def sum_while(location: int, lst: list[int], recorder: int) -> tuple[int, int]:
    maxiter = 600  # len(lst)
    found = False
    while not found:
        if maxiter < recorder:
            return 0, 0
        try:
            p = sum_in_range(lst, location, location + maxiter)
            if is_prime(p) and p < 1000000:
                found = True
            maxiter -= 1
        except IndexError:
            maxiter -= 1
    return maxiter, p


def consecutive_list() -> int:
    limit = 1000000
    primelist = generate_primes(limit)  # ~7 seconds
    max_ = 2

    for i in range(len(primelist)):
        current_length, current_val = sum_while(i, primelist, max_)
        if current_length > max_:
            max_ = current_length
            place = current_val

    return place


if __name__ == '__main__':
    result = timer_wrapper(consecutive_list)
    print(f"{result = }")
