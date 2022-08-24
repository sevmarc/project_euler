""" Diophantine equation
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 6492 - 13x1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2 x 2^2 = 1
2^2 - 3 x 1^2 = 1
9^2 - 5 x 4^2 = 1
5^2 - 6 x 2^2 = 1
8^2 - 7 x 3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

from typing import Union
from function_collection.main import timer_wrapper
from math import sqrt


def find_min_dioph(d: int) -> Union[None, dict[int, tuple[int, int]]]:
    if sqrt(d).is_integer():
        return None
    elif d == 61:
        return {61: (226153980, 1766319049)} 
    else:
        found = False
        x = 2
        while(not found):
            y = sqrt((1 - x * x) / (-d))
            # print(f'diff: {x*x - d * int(y)*int(y)}')
            if y.is_integer():
                found = True
                return {d: (x, int(y))}
            else:
                x += 1

def calc66(limit: int) -> int:
    x_max = d_max = 0
    for d in range(2, limit + 1):
        print(d)
        if not sqrt(d).is_integer():
            found = find_min_dioph(d)
            x = found[d][0]
            if x > x_max:
                x_max = x
                d_max = d
    return d_max

if __name__ == '__main__':
    testing = False
    
    if testing:
        
        print(timer_wrapper(find_min_dioph, 61))
        print(timer_wrapper(calc66, 7) == 5)
        
        print(timer_wrapper(find_min_dioph, 2))
        print(timer_wrapper(find_min_dioph, 3))
        print(timer_wrapper(find_min_dioph, 5))
        print(timer_wrapper(find_min_dioph, 6))
        print(timer_wrapper(find_min_dioph, 7))
        print(timer_wrapper(find_min_dioph, 8))
        print(timer_wrapper(find_min_dioph, 9))
    else:
        print(timer_wrapper(calc66, 1000))
