""" Singular integer right triangles
It turns out that 12 cm is the smallest length of wire that can be bent to 
form an integer sided right angle triangle in exactly one way, but there 
are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an 
integer sided right angle triangle, and other lengths allow more than one 
solution to be found; for example, using 120 cm it is possible to form 
exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1500000 
can exactly one integer sided right angle triangle be formed?
"""

from math import sqrt
from collections import Counter
from function_collection.main import generate_all_pyth_triplets
from function_collection.main import timer_wrapper


def calc75(limit_: int = 1500000) -> int:
    max_generator_input = int(sqrt(int((limit_ / 2))))
    triplets = filter(lambda x: sum(x) <= limit_, generate_all_pyth_triplets(max_generator_input))
    triplet_len_dict = {i: sum(triplet) for i, triplet in enumerate(triplets)}
    
    return len([1 for occurence in Counter(list(triplet_len_dict.values())).values() if occurence == 1])


if __name__ == '__main__':
    testing = False
    
    if testing:
        for p in generate_all_pyth_triplets(10, debug=True):
            print(p)
    else:
        result = timer_wrapper(calc75)
        print(f"{result = }")
