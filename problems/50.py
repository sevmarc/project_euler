# Consecutive prime sum
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

def sum_in_range(lst, start, finish):
    return sum([lst[i] for i in range(start, finish)])

def sum_while(location, lst, recorder):
    maxiter = 600  # len(lst)
    found = False
    while(not found):
        if maxiter < recorder:
            return 0, 0
        try:
            p = sum_in_range(lst, location, location + maxiter)
            if is_prime(p) and p < 1000000:
                found = True
            maxiter -= 1
        except IndexError:
            maxiter -= 1
    return maxiter, p


def consecutive_list():
    limit = 1000000
    primelist = generate_primes(limit)  # ~7 seconds
    max = 2
    for i,p in enumerate(primelist):
        current = sum_while(i, primelist, max)
        current_val = current[1]
        current_lenght = current[0]
        if current_lenght > max:
            max = current_lenght
            place = current_val
    return max, place

start_time = time.time()

print(consecutive_list())

print(time.time() - start_time)