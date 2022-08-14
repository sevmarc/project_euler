""" Lexicographic permutations
A permutation is an ordered arrangement of objects. For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations

if __name__ == '__main__':
    testing = False

    if testing:
        ex_lst = list('012')
        ex = list(permutations(ex_lst))
        print(ex)
    else:
        task_lst = list(range(10))
        task = list(permutations(task_lst))
        ind = 999999
        result = ''.join([str(w) for w in task[ind]])
        print(f"{int(result) = }")
