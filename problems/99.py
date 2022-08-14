"""
Comparing two numbers written in index form like 2**11 and 3**7 is not difficult, 
as any calculator would confirm that 2**11 = 2048 < 3**7 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more difficult, 
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one 
thousand lines with a base/exponent pair on each line, 
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
from function_collection.main import timer_wrapper, exp_by_squaring
from function_collection.utils import handle_filepath
from math import pow
import sys

sys.setrecursionlimit(5000)


def load_base_exp(base_exp):
    exps = []
    with  open(base_exp) as be:
        lines = be.readlines()
        for l in lines:
            exps.append([int(l.split(',')[0]), int(l.split(',')[1].strip('\n'))])
    return exps

"""
    a^b           ?         c^d            ?   e^f
    a*a*a*...*a*a*a     c*c*c*,,*c*c*c        e*e*..*e*e
    d > b
    / /c^b
    (a / c) ^ b   ?         c^(d-b)

    e.g.
    10^3     ?     2^10    ->   (10/2)^3    ?   2^(10-3)
    1000     <     1024            5^3      ?    2^7
                                125      <    126

    a^x   ?   b^x    (a ? b)
    a^x   ?   a^y    (x ? y)


    b < d < f (ordered by exponents)
    a^b           ?         c^d            ?   e^f
    (a^b)/(e^d)           (c/e)^d            e^(f-d)                 /e^d
    (a*e/c)^b / (e^d)     (c/e)^(d-b)        e^(f-d)/(c/e)^b         /(c/e)^b
    (a/c)^b * e^(d-b)     (c/e)^(d-b)        e^(f-d-b) / c^b         /=

    different method:
    a^b        ?       c^d
    a^b * c^(b-d)                   c^b
    c^(b-d)        (c/a)^b     / a^b * c^(d-b)


    -----------------
    a < b
    a^b <> b^a
    a*a*a*a*..*a <> b*b*b*b*...*b
    a^(b-a) <> b^a * a^(-a) = (b/a)^a
    
    -----------------

"""

base_exp = load_base_exp(handle_filepath("inputfiles/99_base_exp.txt"))

def filtering(base_exp):
    for be in base_exp:
        for be2 in base_exp:
            if be[0] > be2[0] and be[1] > be2[1]:  # both numbers are smaller, we remove it
                # print(be, be2)
                base_exp.remove(be2)
    return base_exp

def decreasing_exp_until_smaller(pair_of_be):
    be1_base, be1_exp = pair_of_be[0]
    be2_base, be2_exp = pair_of_be[1]
    # we expect be2_exp > be1_exp
    tolerance = 0.012
    count = 0
    while( abs((be1_exp / be2_exp) - 1) > tolerance):  # they should be close to even:
        count += 1
        print('iter: ', count, be1_exp, be2_exp)
        if be1_exp > be2_exp:
            be1_exp /= 2
            be1_base *= be1_base  # squaring
        else:
            be2_exp /= 2
            be2_base *= be2_base  # squaring
    if be2_base > be1_base:
        print(pair_of_be[1], ' > ', pair_of_be[0])
        return pair_of_be[1]
    if be1_base > be2_base:
        print(pair_of_be[0], ' > ', pair_of_be[1])
        return pair_of_be[0]    
    else:
        return None

def decreasing_exponent(ab, cd):
    a,b = ab
    c,d = cd
    if a > c:
        a /= c
    else:
        c /= a
    if d > b:
        d -= b
    else:
        b -= d
    tolerance = 0.0035
    # print(f"a: {a}, b: {b}, c:{c}, d: {d}")
    if abs(a / c - 1) < tolerance:
        print(f'final! {a, b} > {c, d}')
        try:
            return pow(a,b) > pow(c,d)
        except OverflowError:
            return b > d
    if abs(b / d - 1) < tolerance:
        print(f'final! {a, b} > {c, d} = {a > c}')
        try:
            return pow(a,b) > pow(c,d)
        except OverflowError:
            return a > c
    return decreasing_exponent([a,b], [c,d])
    

def exp(pair_of_be):
    be1_base, be1_exp = pair_of_be[0]
    be2_base, be2_exp = pair_of_be[1]

    temp1_base = be1_base / be2_base
    temp1_exp = be1_exp
    temp2_base = be2_base
    temp2_exp = be2_exp - be1_exp

    res1 = pow(temp1_base, temp1_exp)
    res2 = pow(temp2_base, temp2_exp)
    if res1 > res2:
        print(pair_of_be[0], ' > ', pair_of_be[1] )
        max_ = pair_of_be[0]
    else:
        print(pair_of_be[0], ' < ', pair_of_be[1] )
        max_ = pair_of_be[1]
    
    return max_


def calc99(base_exp):
    max_ = base_exp[-1]
    max_place = None
    for count,current in enumerate(reversed(base_exp)): 
        if count == 0:
            continue
        left = decreasing_exponent(max_, current)
        if not left:
            print(f"loc: {count+1}, [{max_}, {current}], new_max: {current}")
            max_ = current
    print(base_exp.index(max_) + 1)
    return max_

# newbase = filtering(base_exp)

print(timer_wrapper(calc99, base_exp))

# print([newbase[0], newbase[1]])
# print(decreasing_exponent(newbase[0], newbase[1]))
# timer_wrapper(exp, [newbase[0],newbase[1]] )
# print(len(timer_wrapper(filtering, base_exp)))

"""
maxval = timer_wrapper(calc99, newbase)
print('Result: ', base_exp.index(maxval))
"""