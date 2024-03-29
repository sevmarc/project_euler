""" Cuboid route
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 
3, and a fly, F, sits in the opposite corner. 
By travelling on the surfaces of the room the shortest "straight line" 
distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given 
cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring 
rotations, with integer dimensions, 
up to a maximum size of M by M by M, for which the shortest route has 
integer length when M = 100. 
This is the least value of M for which the number of solutions first 
exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first 
exceeds one million.
"""

from function_collection.main import timer_wrapper
from math import sqrt
from copy import copy


def cuboid_paths(sides: list[int]) -> int:
    """
      ___________
     /|_________/|
    | |        | | x
    | |________|_|
    |/_________|/ y
         z
    _______
    |      |
    |      | x + y
    |______|
       z
    The 3 possibilities: pit[x, y+z], [y, x+z], [z, x+y]

    x > y > z
    1) x^2 + (y+z)^2 = x^2 + y^2 + z^2 + 2yz
    2) y^2 + (x+z)^2 = x^2 + y^2 + z^2 + 2xz
    3) z^2 + (x+y)^2 = x^2 + y^2 + z^2 + 2xy
    yz ? xz ? xy / *xyz
    xyz/x < xyz/y < xyz/z (the inverse of original)
    So the shortest path goes for the longest side
    """
    x, y, z = sides
    vals = []
    for side in sides:
        temp = copy(sides)
        temp.remove(side)
        val = sqrt(side**2 + sum(temp)**2)
        vals.append(val)
    return min(vals)


def cuboid_paths_int(sides: list[int]) -> bool:
    x, y, z = sides
    return sqrt(z**2 + (x+y)**2).is_integer()


def generate_unique_cubes(m: int) -> list[int]:
    return [sorted([x, y, z]) for x in range(1, m + 1) for y in range(1, x + 1) for z in range(1, y + 1)]


def new_uniques(m: int) -> list[int]:
    return [sorted([x, y, m]) for x in range(1, m + 1) for y in range(1, x + 1)]


def distinct_cuboids(limit: int) -> int:
    cubes = generate_unique_cubes(limit)
    return len([c for c in cubes if cuboid_paths_int(c)])


def new_distinct_cuboids(limit: int) -> int:
    cubes = new_uniques(limit)
    return len([c for c in cubes if cuboid_paths_int(c)])


def calc86(limit_: int = 1e6) -> int:
    cubes = i = 0

    while (cubes <= limit_):
        i += 1
        cubes += new_distinct_cuboids(i)
    return i


if __name__ == '__main__':
    testing = True

    if testing:
        print(f"{cuboid_paths([3, 5, 7]) = }")
        print(f"{cuboid_paths([3, 5, 6]) = }")
        print(f"{len(generate_unique_cubes(99)) = }")
        print(f"{len(generate_unique_cubes(100)) = }")
        print(timer_wrapper(calc86, 99))
        print(timer_wrapper(calc86, 100))
        print(f"{new_distinct_cuboids(100) = }")
    else:
        print(timer_wrapper(calc86))
