"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest 
cube which has exactly three permutations of its digits which are also 
cube.

Find the smallest cube for which exactly five permutations of its 
digits are cube.
"""

from collections import Counter
from math import pow
from function_collection.main import timer_wrapper


def compare_permutation(arg1: int, arg2: int) -> bool:
    if Counter(str(arg1)) == Counter(str(arg2)):
        return True
    return False


def calc58() -> list[int]:
    n, combination = 10000, 5
    cubes = [int(pow(i, 3)) for i in range(1, n)]
    
    results = []
    for cube in cubes:
        result = [cube]
        for cube2 in cubes:
            if cube2 != cube and compare_permutation(cube, cube2):
                result.append(cube2)
        if len(result) >= combination:
            results.append(result)
            break
    return results


if __name__ == '__main__':
    result = timer_wrapper(calc58)[0][0]
    print(f"{result = }")
