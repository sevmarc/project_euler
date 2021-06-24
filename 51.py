# Prime digit replacements
"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
from math import sqrt
from itertools import permutations
from itertools import chain, combinations
from function_collection import timer_wrapper

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

def next_prime_above(x):
    while 1:
        if is_prime(x):
            return x
        x += 1

def checklist():
    limit = 10000000  # 10000000 = 4583 sec
    num = 1000000000
    n = 8
    #  primelist = generate_primes(limit, limit + num)  # ~7 seconds
    i = 0
    while i < limit:
        p = next_prime_above(i)
        digs = len(str(p))
        opts = create_subset(digs, 2)
        for option in opts:
            if count_primes(switch_chars(p, option)) == n:
                return (switch_chars(p, option), option)
        i = p + 2  # if p was prime, p+1 cant be
print(timer_wrapper(checklist))
