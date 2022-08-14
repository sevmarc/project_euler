""" Consecutive positive divisors
Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""

from function_collection.main import proper_divisors_fast


print(proper_divisors_fast(14))
print(proper_divisors_fast(15))
