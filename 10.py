from math import sqrt

def is_prime(x):
    if x == 1:
        return False
    check = 0
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            check += 1
            if check > 1:
                return False
    if check == 0:
        return True
    else:
        return False


max = 2000000
sum = 0
for i in range(1,max + 1):
    if is_prime(i):
        sum += i

print(sum)