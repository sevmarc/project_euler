from math import sqrt
from itertools import permutations
# Prime permutations

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

def cond1(x1, x2, x3):
    return is_prime(x1) and is_prime(x2) and is_prime(x3)

def word_permutations(x):
    words = []
    for w in list(permutations(str(x))):
        cur = ''
        for l in w:
            cur += l
        words.append(cur)
    return words

jump = 3330
for i in range(1000, 3400):
    j1 = i + jump
    j2 = i + 2 * jump
    if cond1(i, j1, j2):
        # print("PRIMES! ", i, j1, j2)
        if str(j1) in word_permutations(i) and str(j2) in word_permutations(i):
            print("FOUND! ", i, j1, j2)
