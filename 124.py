""" Ordered radicals

The radical of n, rad(n), is the product of the distinct prime factors of n. 
For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting
 on n if the radical values are equal, we get:

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""

from function_collection import timer_wrapper, unique_prime_divisors


def prod(list_of_nums):
    if list_of_nums:
        p = 1
        for i in list_of_nums:
            p *= i
        return p
    else:
        return 1

def rad_n(n: int):
    return prod(unique_prime_divisors(n))

def rad_n_test():
    rads = {}
    limit = 100000
    for i in range(1, limit + 1):
        rads.update( {i: rad_n(i)})
        # print(rad_n(i))
    temp = dict(sorted(rads.items(), key=lambda item: item[1]))
    # print(temp)
    return list(temp)[10000 - 1]  # results position start form 1 instead of 0

print(timer_wrapper(rad_n_test))