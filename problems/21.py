""" Amicable numbers
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are 
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 
11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper 
divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


from math import sqrt
from function_collection.main import proper_divisors_fast


def d(n):
    return sum(proper_divisors_fast(n))


if __name__ == '__main__':
    testing = False
    
    if testing:
        print(f"{d(220) = }")
        print(f"{d(284) = }")
    else:
        max_val = 10000
        result = sum([i for i in range(max_val + 1) if (i == d(d(i))) and (i != d(i))])
        print(f"{result = }")
