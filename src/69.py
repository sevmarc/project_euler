# Totient maximum
from math import sqrt
from math import gcd as bltin_gcd
import time

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

n = 1000000
"""
max = 0
for i in range(2, n):
    f = float(phi(i))
    if i / f > max:
        max = i / f
        place = i
        print(f"{place}: {max}")
print(place)
# 999180: 4.8186
"""
g = generate_primes(n)
prod = 1
count = 0
while(prod < n):
    prod *= g[count]
    f = phi(prod)
    print(count, prod, prod/f)
    count += 1

print(time.time() - start_time)
