from math import pow

def recursive(x):
    """    0  1  2  (2n + 1)
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    """
    if x==0:
        return 1
    sq = pow(2*x+1, 2)
    # return sq + (sq-2*x) + (sq-4*x) + (sq-6*x) + recursive(x - 1)
    return 4 * sq - 12 * x + recursive(x - 1)

print(recursive(0))
print(recursive(1))
print(recursive(2))
print(recursive(3))
size = 1001
n = (size - 1) / 2
print(recursive(n))