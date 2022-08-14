""" Digit fifth powers
Surprisingly there are only three numbers that can be written 
as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the 
sum of fifth powers of their digits.
"""

from math import pow


def checksum(x: int, n: int) -> bool:
    return x == sum([pow(int(l), n) for l in str(x)])


if __name__ == '__main__':
    testing = False

    if testing:
        print(checksum(1634, 4))
        print(checksum(8208, 4))
        print(checksum(9474, 4))
    else:
        max_ = 10000000
        power_ = 5
        
        result = sum([i for i in range(2, max_) if checksum(i, power_)])
        print(f"{result = }")
