"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

import time
from math import gcd as bltin_gcd
from math import sqrt

maximum = 8 # 1000000
counter = 0

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

def calculate_71(x: int):
    counter = 0
    for i in range(2, x + 1):
        counter += phi(i)
    print('Result: ', x,'\t\t', counter)
        


start_time = time.time()

"""
calculate_71(10)
calculate_71(100)
calculate_71(1000)
calculate_71(10000)
calculate_71(100000)
"""
calculate_71(10000000)


print(time.time() - start_time)