# Powerful digit sum
import time
from math import pow

def calc_digits(x):
    return sum([int(w) for w in str(x)])

def iter(limit_a, limit_b):
    max = 0
    for i in range(limit_a):
        for j in range(limit_b):
            cur = calc_digits(int(pow(i, j)))
            if cur > max:
                max = cur
                place = (i, j)
    return max, place

start_time = time.time()

print(iter(100, 100))  # should be 972, too large number cause some trouble

print(time.time() - start_time)