from collections import Counter
from math import pow
import time

start_time = time.time()
n, combination = 10000, 5
cubes = [int(pow(i, 3)) for i in range(1, n)]
results = []

def compare_permutation(arg1, arg2):
    if Counter(str(arg1)) == Counter(str(arg2)):
        return True
    return False

for cube in cubes:
    result = [cube]
    for cube2 in cubes:
        if cube2 != cube:
            if compare_permutation(cube, cube2):
                # print(cube, cube2)
                result.append(cube2)
    if len(result) >= combination:
        results.append(result)
        print(result)
        break

"""
for cube in cubes:
    result = []
    all_perm = set(permutations(str(cube)))
    for perm in all_perm:
        ch = ''.join(perm)
        if ch[0] != '0' and int(ch) in cubes:
                # print(ch, 'is a cube permutation of ', cube)
            result.append(ch)
    if len(result) >= combination:
        results.append(result)
        print(result)
        break
"""
print(results)
print(time.time() - start_time)
