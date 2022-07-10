from math import sqrt
# Distinct primes factors

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

def primes(n, lista=[]):
    if not lista:
        result = []
        if is_prime(n):
            result.append(n)
            return result
    else:
        result = lista
    for i in range(2, n):
        if (n % i) == 0:
            result.append(i)
            n = int(n / i)
            if is_prime(n):
                result.append(n)
                return result
            primes(n, result)
            break
    return result

def prime_dict(n):
    l = primes(n)
    d = {}
    for p in set(l):
        d.update({p: l.count(p)})
    return len(set(sorted(d)))  # d

""""
print(prime_dict(641))
print(prime_dict(642))
print(prime_dict(643))
print(prime_dict(644))
print(prime_dict(645))
print(prime_dict(646))
"""

lookfor = 4
maxval = 1000000
current = 0
for i in range(maxval):
    if prime_dict(i) >= lookfor:
        current += 1
    else:
        current = 0
    if current == lookfor:
        print("FOUND IT!")
        print(i-3, prime_dict(i-3))
        print(i-2, prime_dict(i-2))
        print(i-1, prime_dict(i-1))
        print(i, prime_dict(i))
        break
