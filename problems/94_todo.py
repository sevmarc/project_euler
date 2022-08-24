""" Almost equilateral triangles
It is easily proved that no equilateral triangle exists with integral 
length sides and integral area. 
However, the almost equilateral triangle 5-5-6 has an area of 12 square 
units.

We shall define an almost equilateral triangle to be a triangle for which 
two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with 
integral side lengths and area and whose perimeters do not exceed one 
billion (1,000,000,000).
"""

from function_collection.main import timer_wrapper
from math import pow, sqrt
import decimal


def almost_eq_tri_naive(a: int) -> int:
    b = [a - 1, a + 1]
    """
       #
    a ### a
     ##### 
       b
    perimeter = 2 * a + b
    area = b * ( sqrt(a^2 - (b/2)^2)) ) / 2
    """
    perimeter = []
    area = [(b_ * sqrt(decimal.Decimal(pow(a, 2)) -
                       decimal.Decimal(pow(b_/2, 2))) / 2) for b_ in b]

    """ debugging
    print(f"step 1: pow(a,2) = {decimal.Decimal(pow(a,2))}")
    print(f"step 2: pow(b/2,2) = {decimal.Decimal(pow(b[1]/2,2))}")
    print(f"step 3: pow(a,2) - pow(b[1]/2,2) = {decimal.Decimal(pow(a,2) - pow(b[1]/2,2))}")
    print(f"step 4: sqrt(pow(a,2) - pow(b[1]/2,2) = { decimal.Decimal(np.sqrt(pow(a,2) - pow(b[1]/2,2))) }")
    print(f"step 5: b * sqrt(pow(a,2) - pow(b[1]/2,2) / 2 = { decimal.Decimal(b[1] * np.sqrt(pow(a,2) - pow(b[1]/2,2)) / 2)}")
    print(area)
    """
    for i, area_ in enumerate(area):
        if area_ % 1 == 0:
            # if np.mod(area_, 1) == 0:
            perimeter.append(2 * a + b[i])
    if sum(perimeter):
        print(f'{a}:\t {area} {sum(perimeter)}')
    return sum(perimeter)


def almost_eq_tri(a):
    """
       #|#
    a ##|## a
     ###|### 
       b
    perimeter = 2 * a + b
    area = b * ( sqrt(a^2 - (b/2)^2)) ) / 2

    When is
        (b/2 * m_b) / 2
    an integer?
        (b/2 * m_b)  is even
        1) (b/2) is even OR 2) m_b is even (both int)
        1) (b/2) is even
            b is int
            b is even, if a is odd
            b/2 is even, if a = 4k + 1 or a = 4k + 3 ( a = 2k + 1, odd)
        2) m_b is even
            sqrt(a**2 - (b/2)**2) is even
            a**2 - (b/2)**2 is a square of an even int
            this is part of a pythagorean triple (even), other two being [a, (b/2)]
        example: 5-5-6 -> 6 * sqrt(5**2 - (6/2)**2)/2 = 3 * sqrt(5**2 - 3**2) = 3 * 4 = 12
            b/2 = 3 is not even, so m_b has to be
            [5, 3 , _4_] -> 4 is even, we are good
    """
    blist = [a - 1, a + 1]
    sum_ = 0
    for b in blist:
        two_b_m = sqrt(a**2 - (b/2)**2)
        if (two_b_m % 2 == 0 or b % 2 == 0):
            sum_ += a * 2 + b
    if sum_ or a == 302828:
        print(
            f'{a}:\t [{(sqrt(a**2 - (blist[0]/2)**2)*blist[0]/2)}, {(sqrt(a**2 - (blist[1]/2)**2)*blist[1]/2)}] {sum_}')
    return sum_


def performance_test():
    limit = 10000

    def test1() -> int:
        sum_ = 0
        for i in range(2, int(limit / 3 + 1)):
            sum_ += almost_eq_tri_naive(i)
        print(sum_)
        return sum_

    def test2() -> int:
        sum_ = 0
        for i in range(2, int(limit / 3 + 1)):
            sum_ += almost_eq_tri(i)
        print(sum_)
        return sum_
    print(timer_wrapper(test1) == timer_wrapper(test2))


def calc94(limit_: int = 1000000000) -> int:
    return sum([almost_eq_tri_naive(a) for a in range(2, int(limit_ / 3))])


if __name__ == '__main__':
    testing = False

    if testing:
        performance_test()
        print(almost_eq_tri(5))
        print(almost_eq_tri_naive(48268864))
    else:
        result = timer_wrapper(calc94)
        print(f"{result = }")
