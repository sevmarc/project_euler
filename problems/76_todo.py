""" Counting summations
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two 
positive integers?
--------------------------------------------------------------------


f(x) = 2_sum + f(x-1)
7 = 6 + 1 ; 5 + 2; 4 + 3; (3 + 4...)                    3
8 = 7 + 1 ; 6 + 2; 5 + 3; 4 + 4 ; (3 + 5...)            4
9 = 8 + 1 ; 7 + 2; 6 + 3; 5 + 4 ; (4 + 5...)            4
10 = 9 + 1 ; 8 + 2; 7 + 3; 6 + 4 ; 5 + 5 (4 + 6...)     5



6 - 9
----
5 + 1
4 + 2
3 + 3
4 + 1 + 1
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1


5 - 6
----
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

4 - 4
-----
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1

3 - 2
-----
2 + 1
1 + 1 + 1

2 - 1
-----
1 + 1
"""

from math import floor
from function_collection.main import timer_wrapper


def rec(a):
    if a == 2:
        return 1
    return floor(a / 2) + rec(a-1)


def calc76(n: int = 100) -> int:
    possibilities = sum([rec(i) for i in range(2, n + 1)])
    return possibilities


if __name__ == '__main__':
    result = timer_wrapper(calc76)
    print(f"{result = }")  # 190569291
