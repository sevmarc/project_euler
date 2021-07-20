""" Counting fractions
Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in 
ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 
3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper 
fractions for d ≤ 1,000,000?
"""

from function_collection import unique_prime_divisors, timer_wrapper
from itertools import chain, combinations
from math import gcd as bltin_gcd

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def mult(iterab):
    """Multiply all numbers in the iterable and return result"""
    rv = 1
    for k in iterab:
        rv = rv * k
    return rv



def phi(n:int, printer=False) -> int:
    divs = unique_prime_divisors(n)
    combs = powerset(divs)
    combinations = {}
    for c in combs:
        if len(c) > 1 and mult(c) < n:
            if len(c) in combinations.keys():
                list_at_lenc = combinations[len(c)]
                list_at_lenc.append(mult(c))
                combinations.update( { len(c): list_at_lenc })
            else:
                combinations.update( {len(c): [mult(c)]} )
    if printer:
        print(combinations)
        print(f'n: {n}\t divs: {divs}')
    
    phires = n

    for i in divs:
        if printer:
            print(f'n: {n}\t n/{i} - 1: {(int(n/i) - 1)}\t -> phires: {phires-(int(n/i) - 1)}')
        phires -= (int(n/i) - 1)  # -1 because n not counted in phi
    for lenght, c in combinations.items():
        if lenght % 2 == 0:
            for c_iter in c:
                if printer:
                    print(f'n: {n}\t n/{c_iter} - 1: {(int(n/c_iter) - 1)}\t -> phires: {phires+(lenght - 1)*(int(n/c_iter) - 1)}')
                phires += (int(n/c_iter) - 1)
        else:
            for c_iter in c:
                if printer:
                    print(f'n: {n}\t n/{c_iter} - 1: {(int(n/c_iter) - 1)}\t -> phires: {phires+(lenght - 1)*(int(n/c_iter) - 1)}')
                phires -= (int(n/c_iter) - 1)
    if printer:
        print(f'RETURN: {phires-1}')
    """
    counter = 0
    for i in range(n):
        if bltin_gcd(n, i) == 1:
            counter += 1
    print(f'CHECK: gcd({n},...) = {counter}')
    """
    return phires  # -1 because n not counted in phi

    # old solution, was too slow
    # phi = [i for i in range(1,n) if (bltin_gcd(n, i) == 1)]
    # return len(phi)

def calculate_72(x: int):
    counter = 0
    for d in range(2, x + 1):  # up till x
        counter += phi(d, False)
    print('Result: ', x,'\t\t', counter)
        

testing = False

if __name__ == '__main__':
    if testing:
        # calculate_72(10)
        timer_wrapper(calculate_72, 60)
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
        #   ^   ^   ^   ^    ^     ^     ^     ^    = 8
        #     ^     ^     ^        ^        ^       = 5
        # 1/18, 5/18, 7/18, 11/18, 13/18, 17/18
        
    else:
        timer_wrapper(calculate_72, 1000000)
