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

from function_collection.main import timer_wrapper


def filter_rev(x: int) -> bool:
    """ starts or ends with zero -> not reversible """
    return not (str(x)[0] == '0' or str(x)[-1] == '0')


def reverse(x: int) -> int:
    return int(''.join(reversed(str(x))))


def reversed_sumcheck(x: int) -> bool:
    if filter_rev(x):
        odds = '13579'
        rev_sum = x + reverse(x)
        for l in str(rev_sum):
            return l in odds
        return True
    else:
        return False


def reversed_sumcheck_faster() -> bool:
    """
    Optimization - To be implemented
    Returns:
        bool: True, if reversible
    """
    pass


def calc_145(boundary: int) -> int:
    return len([1 for i in range(boundary) if reversed_sumcheck(i)])


if __name__ == '__main__':
    testing = False

    if testing:
        print(36, reverse(36), reversed_sumcheck(36), filter_rev(36))

    if testing:
        boundary_val = 1000
    else:
        boundary_val = 1000000000

    # runtime ~1870 sec, needs some optimization
    print(timer_wrapper(calc_145, boundary_val))
