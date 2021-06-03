# Spiral primes
from sys import setrecursionlimit
from math import sqrt
import time

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def generate_primes(x):
    return [p for p in range(x) if is_prime(p)]

def recursive(x, corners=[]):
    """    0  1  2  (2n + 1)
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
    if x==0:
        act.append(1)
        return act
    sq = pow(2 * x + 1, 2)
    act.append(sq)
    act.append(sq-2*x)
    act.append(sq-4*x)
    act.append(sq-6*x)
    # return sq + (sq-2*x) + (sq-4*x) + (sq-6*x) + recursive(x - 1)
    return recursive(x - 1, act)

"""
a = recursive(3)
b = recursive(2)
c = recursive(1)
print(a)
print(b)
print(c)
"""

def calculate_primes(l):
    return len([p for p in l if is_prime(p)])

def run_recursion():
    found = False
    current = 3  # 997: crashes, recursion depth
    limit = 10
    while(not found):
        rec = recursive(current)
        percent = calculate_primes(rec) / len(rec) * 100
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

start_time = time.time()

run_recursion()

print(time.time() - start_time)