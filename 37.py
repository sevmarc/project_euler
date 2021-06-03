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

def trunc_left(x: int):
    w = str(x)
    if len(w) > 1:
        return is_prime(x) and trunc_left(int(w[1:]))
    else:
        return is_prime(x)
def trunc_right(x: int):
    w = str(x)
    if len(w) > 1:
        return is_prime(x) and trunc_right(int(w[:len(w)-1]))
    else:
        return is_prime(x)


# test
print(trunc_left(3797))
print(trunc_right(3797))
print(trunc_left(7))

maxval = 1000000
sum = 0
counter = 0
max_counter = 11  # we know this
for i in range(10, maxval):
    if trunc_left(i) and trunc_right(i):
        print(i)
        sum += i
        counter += 1
        if counter == max_counter:
            break

print('SUM: ', sum)
