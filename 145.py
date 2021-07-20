""" How many reversible numbers are there below one-billion?
Some positive integers n have the property that the sum 
[ n + reverse(n) ] consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. 
We will call such numbers reversible; so 36, 63, 409, and 904 
are reversible. Leading zeroes are not allowed in either n 
or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""

from function_collection import timer_wrapper


def filter_rev(x: int) -> bool:
    """ starts or ends with zero -> not reversible """
    if str(x)[0] == '0' or str(x)[-1] == '0':
        return False
    else:
        return True

def reverse(x: int) -> int:
    return int(''.join(reversed(str(x))))

def reversed_sumcheck(x: int) -> bool:
    if filter_rev(x):
        odds = '13579'
        rev_sum = x + reverse(x)
        for l in str(rev_sum):
            # print(l, l not in odds)
            if l not in odds:
                return False
        return True
    else:
        return False

def reversed_sumcheck_faster(x: int) -> bool:
    if filter_rev(x):
        for i in range(len(str(x))):
            pass

def calc_145(boundary: int) -> int:
    sum_ = 0
    for i in range(boundary):
        if reversed_sumcheck(i):
            sum_ += 1
    return sum_


testing = False
if __name__ == '__main__':
    if testing:
        print(36, reverse(36), reversed_sumcheck(36), filter_rev(36))

    if testing:
        boundary_val = 1000
    else:
        boundary_val = 1000000000

    # runtime ~1870 sec, needs some optimization
    print(timer_wrapper(calc_145, boundary_val))