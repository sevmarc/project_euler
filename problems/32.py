# Pandigital products
from collections import Counter
import time

digits = '123456789'

def pandigital(x):
    return Counter(str(x)) == Counter(digits[:len(str(x))])

def pandigital_n(x, n):
    if len(str(x)) != n:
        return False
    return Counter(str(x)) == Counter(digits[:len(str(x))])

"""
# tests
print(pandigital(5))
print(pandigital_n(1234, 4))
print(pandigital_n(1234, 3))
print(pandigital(1))
print(pandigital(23456))
"""

def checker():
    limit_p1 = 10000
    limit_p2 = 10000
    result = []
    for i in range(limit_p1):
        for j in range(limit_p2):
            if pandigital_n(str(i) + str(j) + str(i * j), 9):
                result.append(i*j)
    return sum(set(result))

start_time = time.time()

print(checker())

print(time.time() - start_time)