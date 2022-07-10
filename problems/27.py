from math import sqrt

def is_prime(x):
    if x <= 1:
        return False
    check = 0
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            check += 1
            if check > 0:
                return False
    return True

"""
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
"""

def equa(x, a, b):
    cur = x*x + a*x + b
    # print(cur)
    return is_prime(cur)

def quad(a, b):
    x = 0
    while(equa(x, a, b)):
        x += 1
    return x

# test
# print(quad(-79, 1601))

constr = 1000

max = 0
max_a = 0
max_b = 0

for a in range(-constr, constr):
    for b in range(-constr,constr):
        cur = quad(a,b)
        if cur > max:
            max = cur
            max_a = a
            max_b = b
print(max_a, max_b, ': ', max)
print("Result: ", max_a*max_b)