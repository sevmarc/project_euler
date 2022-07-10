# Non-abundant sums
import time

def proper_divisors(x:int):
    return [i for i in range(1, int(x/2 + 1)) if x % i == 0]
# print(proper_divisors(28))

def deficient(x):
    return x > sum(proper_divisors(x))
def abundant(x):
    return x < sum(proper_divisors(x))
def perfect(x):
    return x == sum(proper_divisors(x))

limit = 28123
abundants = [i for i in range(1, limit + 1) if abundant(i)]
def check_abundant_sum(x, ab=abundants):
    values = [i for i in ab if i < x]
    for v in values:
        if (x - v) in ab:
            # print(v, x-v)  # for actual results
            return True
    return False

def checker():
    sum = 0
    for i in range(1, limit):
        if not check_abundant_sum(i):
            sum += i
    return sum

"""
# tests
print(len(abundants))
print(check_abundant_sum(24))
print(check_abundant_sum(25))
print(check_abundant_sum(23))
"""

start_time = time.time()

print(checker())

print(time.time() - start_time)