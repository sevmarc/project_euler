# Self powers
from math import pow
import time

def exp_by_squaring(x, n):
    if n < 0:
        return exp_by_squaring(1 / x, -n)
    elif n == 0:
        return  1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_squaring(x * x,  n / 2)
    else:
        return x * exp_by_squaring(x * x, (n - 1) / 2)

def summa():
    sum = 0
    iter = 1000
    for i in range(1, iter + 1):
        # print(i)
        sum += int(exp_by_squaring(i, i))
    print(str(sum)[-10:])

start_time = time.time()

summa()

print(time.time() - start_time)