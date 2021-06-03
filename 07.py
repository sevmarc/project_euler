from math import sqrt

# What is the 10 001st prime number?



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

print(is_prime(7))
print(is_prime(13))
print(is_prime(24))
print(is_prime(37))

count = 0
for i in range(1, 1000000):
    if is_prime(i):
        count += 1
        if count == 10001:
            print(count, i)
            break