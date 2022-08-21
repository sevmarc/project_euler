""" Ordered radicals
The radical of n, rad(n), is the product of the distinct prime 
factors of n. 
For example, 504 = 23 x 32 x 7, so rad(504) = 2 x 3 x 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and 
sorting on n if the radical values are equal, we get:

Let E(k) be the kth element in the sorted n column; for example, E(4) 
= 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""

from function_collection.main import timer_wrapper, unique_prime_divisors, listprod


def rad_n(n: int) -> int:
    return listprod(unique_prime_divisors(n))

def rad_n_test(limit_ = 100000) -> int:
    rads = {i: rad_n(i) for i in range(1, limit_ + 1)}
    temp = dict(sorted(rads.items(), key=lambda item: item[1]))
    return list(temp)[10000 - 1]  # results position start form 1 instead of 0

if __name__ == '__main__':
    result = timer_wrapper(rad_n_test)
    print(f"{result = }")