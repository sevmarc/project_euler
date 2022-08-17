""" Powerful digit counts
The 5-digit number, 16807=75, is also a fifth power. 
Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from unicodedata import digit
from function_collection.main import exp_by_squaring, timer_wrapper


def power_counter(debug: bool = False) -> int:
    digit_limit = 100
    limit = 100000
    count = 0
    found = []
    for n in range(1, digit_limit):
        for j in range(1, limit):
            length = len(str(int(exp_by_squaring(j, n))))
            if length > n:
                break
            if n == length:
                found.append([j, n, int(exp_by_squaring(j, n))])
                count += 1
    if debug:
        for f in found:
            print(f)
    return count


def power_counter2() -> int:
    digit_limit = 100
    limit = 100000
    return len([1 for n in range(1, digit_limit) for j in range(1, limit) if n == len(str(int(exp_by_squaring(j, n))))])


if __name__ == '__main__':
    result = timer_wrapper(power_counter)
    print(f"{result = }")
