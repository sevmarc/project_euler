""" Champernowne's constant
An irrational decimal fraction is created by 
concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, 
find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""


def calc40(maxval: int = 1000000) -> int:
    w = ''.join([str(i) for i in range(0, maxval)])

    if (testing := False):
        print(f"{w[12] = }")
        print(f"{w[5] = }")

    prod = 1
    for n in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        prod *= int(w[n])
    return prod


if __name__ == '__main__':
    result = calc40()
    print(f"{result = }")
