""" Spiral primes
Starting with 1 and spiralling anticlockwise in the following 
way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the 
bottom right diagonal, but what is more interesting is that 8 out 
of the 13 numbers lying along both diagonals are prime; that is, 
a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a 
square spiral with side length 9 will be formed. If this process 
is continued, what is the side length of the square spiral for 
which the ratio of primes along both diagonals first falls below 
10%?
"""

from function_collection.main import is_prime
from function_collection.main import timer_wrapper


def recursive(x, corners=[]):
    """    
    0  1  2  (2n + 1)
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49
    """
    if corners == []:
        act = []
    else:
        act = corners
    if x == 0:
        act.append(1)
        return act
    sq = pow(2 * x + 1, 2)
    act.append(sq)
    act.append(sq-2*x)
    act.append(sq-4*x)
    act.append(sq-6*x)
    return recursive(x - 1, act)


def calc58_lin(target_percent: float = 0.1) -> int:
    """
    0 -> 1
    1 -> 3, 5, 7, 9
    2 -> 13, 17, 21, 25
    3 -> 31, 37, 43, 49
    """
    prime_total = (0, 1)
    x = 1
    while True:
        sq = (2*x + 1)**2
        current_list = [sq-2*x, sq-4*x, sq - 6*x]  # sq not prime

        prime_total = (
            prime_total[0] + count_primes(current_list), prime_total[1] + 4)

        if prime_ratio_tuple(prime_total) <= target_percent:
            return 2*x + 1
        x += 1


def count_primes(l: list[int]) -> int:
    return len(list(filter(lambda x: is_prime(x), l)))


def prime_ratio(l: list[int]) -> float:
    return float(count_primes(l)) / len(l)


def prime_ratio_tuple(t: tuple[int, int]) -> float:
    return float(t[0]) / t[1]


def run_recursion() -> None:
    found = False
    current = 3  # 997: crashes, recursion depth
    limit = 10
    while (not found):
        rec = recursive(current)
        percent = count_primes(rec) / len(rec) * 100
        print(current, percent, '%')
        if percent <= limit:
            found = True
        if abs(percent - limit) > 1:
            current += 1000
        if abs(percent - limit) > 0.4:
            current += 100
        elif abs(percent - limit) > 0.1:
            current += 10
        else:
            current += 1
    print("Vois la! length: ", (current-1) * 2 + 1)


if __name__ == '__main__':
    testing = False

    if testing:
        print(f"{recursive(3)}")
        print(f"{recursive(2)}")
        print(f"{recursive(1)}")
    else:
        result = timer_wrapper(calc58_lin, 0.1)  # ~1 sec
        print(f"{result = }")
