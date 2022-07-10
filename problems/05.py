""" Smallest multiple
2520 is the smallest number that can be divided by each of 
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
"""

from function_collection.main import is_prime

"""
1*2*3*4*5*6*7*8*9*10
1*2*3*(2*2)*5*(2*3)*7*(2*2*2)*(3*3)*(2*5)
X 2 3  X 2  5  X X  7  X X 2   X 3   X X
highest order of prime in one occurence
"""

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

def prime_dict(n: int) -> dict[int: int]:
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

print(prime_dict(10))
print(prime_dict(20))
print(prime_dict(24))
print(prime_dict(7))
"""

run_example = False
if run_example:
    ex = common(range(1,10))
    print(ex)
    prod = 1
    for i,j in ex.items():
        prod *= (i**j)
    print(prod)


if __name__ == '__main__':
    task = common(range(1,20))
    
    prod = 1
    for i,j in task.items():
        prod *= (i**j)
    print(prod)
