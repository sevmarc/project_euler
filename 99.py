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
from math import pow

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


"""

base_exp = load_base_exp("inputfiles/99_base_exp.txt")

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
    tolerance = 0.2
    count = 0
    while( abs((be1_exp / be2_exp) - 1) > 0.01):  # they should be close to even:
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
    max_ = base_exp[0]
    max_place = None
    for count,current in enumerate(base_exp): 
        if count == 0:
            continue
        # max_ = exp([max_, current] )
        max_ = decreasing_exp_until_smaller([max_, current])
    return max_

newbase = filtering(base_exp)
print(timer_wrapper(decreasing_exp_until_smaller, [newbase[0], newbase[1]]))
# timer_wrapper(exp, [newbase[0],newbase[1]] )
# print(len(timer_wrapper(filtering, base_exp)))

"""
maxval = timer_wrapper(calc99, newbase)
print('Result: ', base_exp.index(maxval))
"""