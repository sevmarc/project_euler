""" Prime power triples
The smallest number expressible as the sum of a prime square, prime 
cube, and prime fourth power is 28. In fact, there are exactly four 
numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a 
prime square, prime cube, and prime fourth power?
"""

from function_collection.main import timer_wrapper, generate_primes
from math import sqrt


def calc87(limit_: int = int(50e6)) -> int:
    pr_list = generate_primes(int(sqrt(limit_)) + 1)
    pr_pow_sums = []
    for p1 in pr_list:
        for p2 in pr_list:
            for p3 in pr_list:
                pr_pow_sum = p1**2 + p2**3 + p3**4
                if pr_pow_sum not in pr_pow_sums and pr_pow_sum < limit_:
                    pr_pow_sums.append(pr_pow_sum)
    return len(pr_pow_sums)


if __name__ == '__main__':
    result = timer_wrapper(calc87)
    print(f"{result = }")
