from math import sqrt

def triangle(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

"""
print(triangle(1))
print(triangle(4))
print(triangle(5))
print(triangle(6))
"""

def divisors(x):
    count = 2  # x and 1 not checked, always divisor
    for i in range(2, int(x / 2) + 1):
        if (x % i) == 0:
            count += 1
    return count

"""
print(divisors(triangle(4)))
print(divisors(triangle(5)))
print(divisors(triangle(6)))
print(divisors(triangle(7)))
"""

def is_prime(x):
    if x == 1:
        return False
    check = 0
    for i in range(1, x+1):
        if x % i == 0:
            check += 1
            if check > 2:
                return False
    if check == 2:
        return True
    else:
        return False

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
    return d

def divisors_fast(n):
    div = 1
    for i,j in prime_dict(n).items():
        div *= (j+1)
    return div

# print(divisors_fast(triangle(7)))


for i in range(1,100000):
    if divisors_fast(triangle(i)) >= 500:
        print(i, triangle(i))
        break