def moveset(n, m):
    if (n == 0) or (m == 0):
        return 1
    return moveset(n-1,m) + moveset(n,m-1)

def moveset2(n,m):
    sum = 0
    for i in range(n+1):
        sum += i
    for i in range(m+1):
        sum += i
    return sum

def moveset3(n,m):
    sum = 0
    for i in range(n+1):
        sum += i
    return 2 * sum

"""
print(1, moveset(1,1))
print(moveset(1,2))
print(moveset(2,1))
print(2, moveset(2,2))
print(3,moveset(3,3))
print(4,moveset(4,4))
print(5,moveset(5,5))
print(6,moveset(6,6))
print(7,moveset(7,7))
print(8,moveset(8,8))
print(9,moveset(9,9))
print(10,moveset(10,10))
"""
"""
for i in range(1,15):
    old = moveset(i-1,i-1)
    cur = moveset(i,i)
    print(i, cur, cur/old)
"""
# print(moveset(20,20))

def fact(x):
    if x == 1:
        return 1
    else:
        return (x) * fact(x-1)


def trial(x):
    if x == 1:
        return 2
    return (8*x-4)/(2*x)*trial(x-1)

"""
for i in range(2,15):
    print(i, trial(i))
"""

print(trial(20))

