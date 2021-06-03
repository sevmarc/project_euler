import time
from math import pow


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

def power_counter():
    digit_limit = 100
    limit = 100000
    count = 0
    found = []
    for n in range(1, digit_limit):
        for j in range(1, limit):
            length = len(str(int(exp_by_squaring(j, n))))
            if length > n:
                break
            if n == length:
                found.append([j, n, int(exp_by_squaring(j, n))])
                count += 1
    for f in found:
        print(f)
    print(count)

start_time = time.time()

power_counter()

print(time.time() - start_time)