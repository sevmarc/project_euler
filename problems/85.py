""" Counting rectangles
By counting carefully it can be seen that a rectangular grid measuring 3 
by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution.
"""

from function_collection.main import timer_wrapper

"""
1x1 -> 1  (1)
2x1 -> 3  (2 + 1)
2x2 -> 9  (4 + 2 + 2 + 1)
3x1 -> 6  (3 + 2 + 1)
3x2 -> 18 (6 + 4 + 2 + 3 + 2 + 1)
3x3 -> 36 (9 + 6 + 3 + 6 + 4 + 2 + 3 + 2 + 1)
"""


def calc_rects(sides: list[int], acc: int = 0) -> int:
    x, y = sides
    curr = acc
    if y >= 1:
        curr += sum(range(x+1)) * y
        return calc_rects([x, y-1], curr)
    else:
        return curr


def calc85(debug: bool = False) -> int:
    est = 2e6
    minimum = 10000
    for i in range(100):
        for j in range(i):
            current = calc_rects([i, j])
            if abs(current - est) < minimum:
                minimum = abs(current - est)
                place = [i, j]
    if debug:
        print(place, calc_rects(place), '; area: ', place[0] * place[1])
    return place[0] * place[1]


if __name__ == '__main__':
    testing = False

    if testing:
        print(timer_wrapper(calc_rects, [1, 1]))
        print(timer_wrapper(calc_rects, [2, 1]))
        print(timer_wrapper(calc_rects, [2, 2]))
        print(timer_wrapper(calc_rects, [3, 1]))
        print(timer_wrapper(calc_rects, [3, 2]))
        print(timer_wrapper(calc_rects, [3, 3]))
    else:
        result = timer_wrapper(calc85)
        print(f"{result = }")
