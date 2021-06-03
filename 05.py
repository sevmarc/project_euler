from math import sqrt

# print(4*7*9*10)
"""
1*2*3*4*5*6*7*8*9*10
1*2*3*(2*2)*5*(2*3)*7*(2*2*2)*(3*3)*(2*5)
X 2 3  X 2  5  X X  7  X X 2   X 3   X X
highest order of prime in one occurence
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

def common(l):
    d = {}
    for n in l:
        for i,j in prime_dict(n).items():
            try:
                if d[i] < j:
                    d.update({i: j})
            except KeyError:
                d.update({i: j})
    return d
"""
# test
print(primes(10))
print(primes(20))
print(primes(24))
"""
print(prime_dict(10))
print(prime_dict(20))
print(prime_dict(24))

print(prime_dict(7))

taskl = range(1,20)
exl = range(1,10)
print(taskl)

ex = common(exl)
print(ex)
prod = 1
for i,j in ex.items():
    prod *= (i**j)
print(prod)


task = common(taskl)
print(task)
prod = 1
for i,j in task.items():
    prod *= (i**j)
print(prod)

