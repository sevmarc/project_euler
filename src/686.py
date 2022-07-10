import time
from math import pow, log


def exp_by_squaring(x, n):
    if n < 0:
        return exp_by_squaring(1 / x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_by_squaring(x * x,  n / 2)
    else:
        return x * exp_by_squaring(x * x, (n - 1) / 2)


def second_powers(n: int):
    return [int(exp_by_squaring(2, i)) for i in range(1, n)]


def p(L: int, n: int, powlist) -> int:
    # lista = [i for i in powlist if str(i).startswith(str(L))]
    # return int(log(lista[n - 1], 2))
    counter = 0
    num = 0
    while(true):
        sq = exp_by_squaring(2, num)
        if str(sq).startswith(str(L)):
            counter += 1
            if counter == n:
                return num
        num += 1


start_time = time.time()

powers = second_powers(26000)
print(p(12, 1, powers))
print(p(12, 2, powers))
print(p(123, 45, powers))

print(time.time() - start_time)
