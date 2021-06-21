from math import sqrt
from math import gcd as bltin_gcd
import time

#-------------------------primes-------------------------
def is_prime(x: int) -> bool:
    """ Checks if a number is prime """
    if x <= 1:
        return False
    check = 0
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            check += 1
            if check > 0:
                return False
    return True

def unique_prime_divisors(x, primes=[]):
    """ Returns a set of all prime divisors """
    if primes:
        temp = primes
    else:
        temp = []
    if is_prime(x):
        temp.append(x)
        return set(temp)
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            temp.append(i)
            return unique_prime_divisors(int(x / i), temp)

def generate_primes(x):
    """ Return a list of primes up to input (x) """
    return [i for i in range(1,x) if is_prime(i)]


#-------------------------exponents-------------------------
def exp_by_squaring(x, n):
    """ Faster method for exponents, using squaring """
    if n < 0:
        return exp_by_squaring(1 / x, -n)
    elif n == 0:
        return  1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_squaring(x * x,  n / 2)
    else:
        return x * exp_by_squaring(x * x, (n - 1) / 2)

def timer_wrapper(f, args=None):
    start_time = time.time()
    if args:
        a = f(args)
    else:
        a = f()
    print('Elapsed time: ', time.time() - start_time)
    return a

#-------------------------divisors-------------------------
def proper_divisors(x:int):
    return [i for i in range(1, int(x/2 + 1)) if x % i == 0]

def proper_divisors_fast(x:int):
    div = [1]  # everything is divisible by 1
    looking_limit = int(x / 2 + 1)
    current = 2

    while current < looking_limit:
        if x % current == 0:
            div.append(current)
            other_div = int(x / current)
            div.append(other_div)
            looking_limit = other_div
        current += 1
    return list(set(div))

def is_perfect(x: int) -> bool:
    return sum(proper_divisors_fast(x)) == x

