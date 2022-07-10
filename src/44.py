# Pentagon numbers

from math import sqrt

limit = 10000
def penta():
    p = []
    for i in range(1, limit+1):
        p.append(int(i * (3 * i - 1) / 2))
    return p

def check_penta(x: int):
    n = (1 + sqrt(1 + 24 * x) ) / 6
    return n.is_integer()

n = penta()
# print(n)
"""
print(check_penta(92))
print(check_penta(145))
print(check_penta(4))
"""

min = 1000000000
D = 0
for i in range(1, limit):
    for j in range(1, limit):
        # print(n[i] + n[j], (n[i] + n[j]) in n)
        if check_penta(n[i] + n[j]) and check_penta(abs(n[j] - n[i])):
            print("found one! ", n[i], n[j])
            d = abs(n[i] - n[j])
            if d < min:
                min = d
                D = d
print("FOUND: ", D, ' with ', min)