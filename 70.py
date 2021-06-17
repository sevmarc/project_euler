# Totient maximum
from math import sqrt
from math import gcd as bltin_gcd
import time
from collections import Counter

def compare_permutation(arg1, arg2):
    return Counter(str(arg1)) == Counter(str(arg2))

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

def generate_primes(x):
    pr = [i for i in range(1,x) if is_prime(i)]
    return pr

def phi(n:int):
    divs = unique_prime_divisors(n)
    phires = n

    for i in divs:
        phires -= (int(n/i) - 1)  # -1 because n not counted in phi
    return phires - 1  # -1 because n not counted in phi

    # old solution, was too slow
    # phi = [i for i in range(1,n) if (bltin_gcd(n, i) == 1)]
    # return len(phi)

def unique_prime_divisors(x, primes=[]):
    if primes:
        temp = primes
    else:
        temp = []

    if is_prime(x):
        temp.append(x)
        return set(temp)
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            temp.append(i)
            return unique_prime_divisors(int(x / i), temp)

def proper_divisors(x:int):
    divlist = [i for i in range(2, int(x/2 + 1)) if x % i == 0]
    res = divlist
    for div in divlist:
        if not is_prime(div):
            for j in proper_divisors(div):
                if j not in res:
                    res.append(j)
    return res

start_time = time.time()

n = 10000000
min = 1000
for i in range(2, n):
    print(i)
    f = phi(i)
    if compare_permutation(i, f):
        if float(i / f) < min:
            min = float(i / f)
            place = i
            print(f"{place}: {min}")
print(f"Winner: {place}: {min}")

"""
tests
print(proper_divisors(125))
print(proper_divisors(625))
print('125 ' , prime_div(125))
print('25 ', prime_div(25))
print('5 ', prime_div(5))

print(phi(9))
print(phi(87109))
"""

print(time.time() - start_time)
