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


start_time = time.time()

number = 28433 * exp_by_squaring(2, 7830457) + 1
print(str(number)[-10:])

print(time.time() - start_time)