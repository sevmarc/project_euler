# Pandigital prime

from math import sqrt
from itertools import permutations

def is_prime(x):
    if x <= 1:
        return False
    check = 0
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            check += 1
            if check > 0:
                return False
    return True

def scramble(x: str):
    lst = list(permutations(x))
    return lst

digits = "123456789"
max = 0
for i in range(1, len(digits) + 1):
    for s in scramble(digits[:i]):
        u = ''
        for l in s:
            u += l
        if is_prime(int(u)) and int(u) > max:
            max = int(u)
print(max)
