from math import sqrt
# circular primes

def circulate(x: int):
    w = str(x)
    circ = []
    circ.append(x)
    for i in range(len(w)):
        cur = w[i:] + w[:i]
        # print(cur)
        circ.append(int(cur))
    return circ

# test
# circulate(197)
#circulate(1234)


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

def check_circ(l):
    for i in l:
        if not is_prime(i):
            return False
    return True
testval = 100
counter = 0
for i in range(2, testval):
    if check_circ(circulate(i)):
        counter += 1

print("counter: ", counter)

maxval = 1000000
counter = 0
for i in range(2, maxval):
    if check_circ(circulate(i)):
        counter += 1

print("counter: ", counter)