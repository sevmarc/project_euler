from math import sqrt

def d(n):
    sum = 1
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            sum += i
            sum += int(n/i)
    return sum

def divisors(x):
    count = 2  # x and 1 not checked, always divisor
    for i in range(2, int(x / 2) + 1):
        if (x % i) == 0:
            count += 1
    return count

# test
# print(d(220))
# print(d(284))

max_val = 10000
sum = 0
for i in range(max_val+1):
    if (i == d(d(i))) and (i != d(i)):
        sum += i

print(sum)