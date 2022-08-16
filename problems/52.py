""" Permuted multiples
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 
5x, and 6x, contain the same digits.
"""

from collections import Counter
from function_collection.main import timer_wrapper


def compare_counters(lst: list[int]) -> bool:
    for ind in range(len(lst) - 1):
        if Counter(str(lst[ind])) != Counter(str(lst[ind + 1])):
            return False
    return True


def calc52() -> int:
    m = [1, 2, 3, 4, 5, 6]
    maxval = 1000000

    result = list(filter(lambda x: compare_counters(x), [[mult * i for mult in m]
              for i in range(10, maxval)]))[0][0]
    return result


if __name__ == '__main__':
    testing = False

    if testing:
        print(Counter("asd") == Counter("dsa"))
    else:
        result = timer_wrapper(calc52)
        print(f"{result = }")
