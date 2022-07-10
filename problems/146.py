""" Investigating a Prime Pattern
The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
"""

from function_collection.main import is_prime, timer_wrapper, generate_primes

"""
(n^2 + 1) is prime=odd -> n^2 is even -> n is even
"""

def solution():
    max_lim = 10000
    ns = []
    for n in range(2, max_lim, 2):
        all_primes = True
        for j in [n*n + 1, 
                  n*n + 3, 
                  n*n + 7,
                  n*n + 9,
                  n*n + 13,
                  n*n + 27]:
            if not is_prime(j):
                all_primes = False
                break
        if all_primes:
            ns.append(n)
            print(n)
    print(sum(ns))

timer_wrapper(solution)
timer_wrapper(generate_primes, 10000)
# timer_wrapper(solution)