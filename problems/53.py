""" Combinatoric selections
https://projecteuler.net/problem=53
"""

from function_collection.main import fact_recursive
from function_collection.main import timer_wrapper


def below(n: int, r: int) -> int:
    return int(fact_recursive(n) / (fact_recursive(r) * fact_recursive(n - r)))


def calc53() -> int:
    limit = 1000000
    result_list = [(i, j) for i in range(1, 101)
                   for j in range(1, i) if below(i, j) > limit]
    return len(result_list)


if __name__ == '__main__':
    testing = False

    if testing:
        print(below(5, 3))
        print(below(23, 10))
    else:
        result = timer_wrapper(calc53)
        print(f"{result = }")
