# Prime digit replacements
from math import sqrt
from itertools import permutations
from itertools import chain, combinations
import time


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def generate_primes(arg1, arg2):
    return [i for i in range(arg1, arg2) if is_prime(i)]

def count_primes(lst):
    return len([i for i in lst if is_prime(int(i))])

def switch_chars(p, ch):
    nums = []
    ls = list(str(p))
    start = 0
    if 0 in ch:
        start = 1
    for i in range(start, 10):
        ls[ch[0]] = str(i)
        ls[ch[1]] = str(i)
        nums.append(int(''.join(ls)))
    return nums

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def create_subset(l, n):
    return [i for i in powerset(range(l)) if (len(i) == n) ]

def checklist():
    limit = 100000000  # 10000000 = 4583 sec
    num = 10000000
    n = 8
    primelist = generate_primes(limit, limit + num)  # ~7 seconds

    for p in primelist:
        digs = len(str(p))
        opts = create_subset(digs, 2)
        for option in opts:
            if count_primes(switch_chars(p, option)) == n:
                return (switch_chars(p, option), option)

start_time = time.time()
result = checklist()
print(result)
print(time.time() - start_time)
