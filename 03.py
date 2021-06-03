from math import sqrt

def factors(n):
    factors = []
    for i in range(2, int(n/6) + 1):
        if (n % i) == 0:
            factors.append(i)
    return factors

def is_prime(x):
    check = 0
    for i in range(1, int(sqrt(x) + 1)):
        if x % i == 0:
            check += 1
            if check > 1:
                return False
    if check == 1:
        return True
    else:
        return False

def max_prime_factor(n):
    max = 0
    for elem in factors(n):
        if is_prime(elem):
            max = elem
    return max

def faster(n):
    max = 1
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            n = n / i
            if is_prime(i):
                max = i
    return max

# test
print(faster(24))
print(faster(13195))
print(faster(600851475143))

"""
print(max_prime_factor(24))
print(max_prime_factor(13195))

print(max_prime_factor(600851475143))
"""