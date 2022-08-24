""" Totient maximum
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of numbers less than n which are 
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all 
less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                1      	2
3	1,2	                2	    1.5
4	1,3	                2	    2
5	1,2,3,4	            4   	1.25
6	1,5	                2   	3
7	1,2,3,4,5,6	        6   	1.1666...
8	1,3,5,7	            4    	2
9	1,2,4,5,7,8	        6   	1.5
10	1,3,7,9	            4   	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

from math import gcd as bltin_gcd
from function_collection.main import is_prime, generate_primes, proper_divisors_fast, unique_prime_divisors
from function_collection.main import timer_wrapper


def phi_exp(n: int) -> int:
    print(f"{n}: {proper_divisors_fast(n) = }")
    return n - len(proper_divisors_fast(n))

def phi(n: int) -> int:
    phi = [i for i in range(1, n) if (bltin_gcd(n, i) == 1)]
    return len(phi)


def phi2(n: int) -> int:
    return n - sum([(int(n/i) - 1) for i in unique_prime_divisors(n)]) - 1


def calc69() -> int:
    n = 1000000
    g = generate_primes(n)
    prod = 1
    count = 0

    while (prod < n):
        prod *= g[count]
        print(count, prod, prod/phi(prod))
        count += 1
    return prod


if __name__ == '__main__':
    testing = False
    
    if testing:
        for i in range(2, 11):
            print(f"{i}: {phi_exp(i) = }\t{i/phi_exp(i)}")
    else:   
        result = timer_wrapper(calc69)
        print(f"{result = }")
