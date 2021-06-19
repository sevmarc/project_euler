"""
Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2 × 2^2 = 1
2^2 – 3 × 1^2 = 1
9^2 – 5 × 4^2 = 1
5^2 – 6 × 2^2 = 1
8^2 – 7 × 3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

from function_collection import timer_wrapper
from math import sqrt


def find_min_dioph(D: int):
    if sqrt(D).is_integer():
        return None
    else:
        found = False
        x = 2
        while(not found):
            y = sqrt((1 - x * x) / (-D))
            if y.is_integer():
                found = True
                print(f"D: {D}, X: {x}, Y: {int(y)}")
                return x, y
            else:
                x += 1

def calc66():
    max_ = 1000
    x_max = 0
    for d in range(2, max_ + 1):
        found = find_min_dioph(d)
        if found:
            x = found[0]
            if x > x_max:
                x_max = x
                print(x_max)
    print(x)
    return x

"""
timer_wrapper(find_min_dioph, 2)
timer_wrapper(find_min_dioph, 3)
timer_wrapper(find_min_dioph, 5)
timer_wrapper(find_min_dioph, 6)
timer_wrapper(find_min_dioph, 7)
"""
timer_wrapper(calc66)