""" Integer right triangles
If p is the perimeter of a right angle triangle with 
integral length sides, {a,b,c}, there are exactly 
three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from function_collection.main import check_pyth
from function_collection.main import timer_wrapper


def perims(p: int) -> list[int]:
    def setter(l: list[int]) -> list[int]:
        cur = []
        for i in l:
            if i not in cur:
                cur.append(i)
        return cur

    raw_results = [sorted([i, j, p - i - j]) for i in range(1, p)
                   for j in range(1, p) if (i + j) < p and check_pyth(i, j, p - i - j)]
    return setter(raw_results)


def calc39(p: int = 1000) -> int:
    max_ = 0
    for i in range(p):
        cur = perims(i)
        if len(cur) > max_:
            max_ = len(cur)
            place = i
    return place


if __name__ == '__main__':
    testing = False

    if testing:
        perimeter = 120
        print(f"{perims(perimeter) = }")
    else:
        result = timer_wrapper(calc39)
        print(f"{result = }")
