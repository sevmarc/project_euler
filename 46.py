# Goldbach's other conjecture
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

def check_goldbach(x: int):
    for i in range(x):
        if is_prime(i):
            if sqrt((x - i) / 2).is_integer():
                print(x , " == ", i, ' + 2 x ', int(sqrt((x - i)/2)), "^ 2")
                return True
    return False

maxval = 100000
for i in range(2, maxval):
    cur = 2 * i - 1
    if not is_prime(cur):
        print(cur , check_goldbach(cur))
        if not check_goldbach(cur):
            print("FOUND IT! ", cur)
            break
