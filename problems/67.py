""" Maximum path sum I
By starting at the top of the triangle below and moving to adjacent  numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click
and 'Save Link/Target As...'), a 15K text file containing a triangle 
with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not 
possible to try every route to solve this problem, as there are 299 
altogether! If you could check one trillion (1012) routes every second 
it would take over twenty billion years to check them all. There is an 
efficient algorithm to solve it. ;o)
"""

from function_collection.main import timer_wrapper
from function_collection.utils import handle_filepath


def str_to_int(tri: list[list[str]]) -> list[list[int]]:
    return [[int(val) for val in row] for row in tri]


def read_triangle_from_file(f: str) -> list[list[int]]:
    return str_to_int([(line.replace('\n', '').split(' ')) for line in open(f, 'r')])


def find_best_path(tri: list[list[str]]) -> int:
    counter = 0
    for i in range(len(tri)-2, -1, -1):
        for j in range(len(tri[i])):
            tri[i][j] = tri[i][j] + max(tri[i+1][j], tri[i+1][j+1])
            counter += 1
        tri.pop()
    print('Found {} in {} iterations'.format(tri[0][0], counter))
    return counter


if __name__ == '__main__':
    triangle = read_triangle_from_file(handle_filepath("inputfiles/67.txt"))
    result = timer_wrapper(find_best_path, [triangle])
    print(f"{result = }")