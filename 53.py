# Combinatoric selections
from math import sqrt, prod

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def below(n, r):
    # np = prod([i for i in range(n,r-1,-1)])
    # rp = prod([i for i in range(1, r+1)])
    return int(fact(n) / ( fact(r) * fact(n - r) )) # float(np) / rp

print(below(5, 3))
print(below(23, 10))

def checking():
    limit = 1000000
    result = []
    for i in range(1, 101):
        for j in range(1, i):
            if below(i , j) > limit:
                result.append((i, j))
    print(result)
    print(len(result))

checking()