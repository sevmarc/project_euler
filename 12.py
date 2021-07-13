""" Highly divisible triangular number
The sequence of triangle numbers is generated by adding 
the natural numbers. So the 7th triangle number would be 
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have 
over five divisors.

What is the value of the first triangle number to have 
over five hundred divisors?
"""

from function_collection import is_prime, timer_wrapper


def triangle(n: int) -> int:
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

def divisors(x: int) -> int:
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

def primes(n: int, lista=[]) -> list[int]:
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

def divisors_fast(n: int) -> int:
    div = 1
    for i,j in prime_dict(n).items():
        div *= (j+1)
    return div
# print(divisors_fast(triangle(7)))


def calc12():
    for i in range(1,100000):
        if divisors_fast(triangle(i)) >= 500:
            print(i, triangle(i))
            break

if __name__ == '__main__':
    timer_wrapper(calc12)
