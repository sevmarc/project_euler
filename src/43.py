# Sub-string divisibility
from collections import Counter
from itertools import permutations

digits = "0123456789"
explen = 10

def pandigital(w):
    if len(w) != 10:
        return False
    for i,j in Counter(w).items():
        if j != 1 or i not in digits:
            return False
    return True

"""
# test
print(pandigital("1406357289"))
print(pandigital("1403257869"))
print(pandigital("14063249"))
print(pandigital("1234"))
"""

def cond(w, d1, d2, d3, div):
    return int(w[d1 - 1] + w[d2 - 1] + w[d3 - 1]) % div == 0

def cond1(w):
    return cond(w, 2, 3, 4, 2)
def cond2(w):
    return cond(w, 3, 4, 5, 3)
def cond3(w):
    return cond(w, 4, 5, 6, 5)
def cond4(w):
    return cond(w, 5, 6, 7, 7)
def cond5(w):
    return cond(w, 6, 7, 8, 11)
def cond6(w):
    return cond(w, 7, 8, 9, 13)
def cond7(w):
    return cond(w, 8, 9, 10, 17)

sum = 0
for j in list(permutations(digits)):
    if pandigital(j):
        if cond1(j) and cond2(j) and cond3(j) and cond4(j) and cond5(j) and cond6(j) and cond7(j):
            w = ''
            for l in j:
                w += l
            print(w)
            sum += int(w)
print("RESULT: ", sum)
