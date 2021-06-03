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
    phi = [i for i in range(1,n) if (bltin_gcd(n, i) == 1)]
    return len(phi)

start_time = time.time()

n = int(10e7)
min = 1000
for i in range(2, n):
    f = float(phi(i))
    if compare_permutation(i, f) and i / f < min:
        min = i / f
        place = i
        print(f"{place}: {min}")

print(time.time() - start_time)
