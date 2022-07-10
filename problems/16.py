""" Power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from math import sqrt

def powdig(x: int,y: int) -> int:
    val = pow(x,y)
    sum_ = 0
    for w in str(val):
        sum_ += int(w)
    return sum_

if __name__ == '__main__':
    # print(powdig(2, 15))
    print(powdig(2, 1000))
