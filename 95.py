"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

from function_collection import timer_wrapper, proper_divisors, proper_divisors_fast

def test1(x):
    for i in range(x):
        print(i, proper_divisors(i))

def test2(x):
    for i in range(x):
        print(i, proper_divisors_fast(i))
        
def test3(x):
    for i in range(x):
        print(i, amicable_chain1(i))

def test4(x):
    for i in range(x):
        print(i, amicable_chain2(i))
        
def is_perfect(x: int):
    return sum(proper_divisors_fast(x)) == x


def amicable_chain1(start: int):
    last = start
    current = 0
    results = []
    limit = 1000000

    while(current != start):
        results.append(last)
        current = sum(proper_divisors_fast(last))
        last = current
        print(current)
        if is_perfect(current) or (current > limit):
            print('FOUND: ', current)
            current = start
            results = []
    if results:
        # print(len(results), results, min(results))
        return len(results), min(results)
    else:
        # print(0, None)
        return (0, None)

def amicable_chain2(start: int):
    last = start
    current = 0
    length = 0

    while(current != start):
        current = sum(proper_divisors_fast(last))
        # print(length, current)
        last = current
        length += 1
        if is_perfect(current):
            current = start
            length = 0
    # print(length)
    return length

def amicable_chain_recursive(start: int, data, acc=[]):
    limit = 1000000

    current = sum(proper_divisors_fast(start))

    if len(data) > current:
        return 0, None

    if acc:
        results = acc
    else:
        results = [start]


    if current in results[1:] or (current > limit):  # or is_perfect(current) 
        if is_perfect(current) or current > limit or results[0] not in results[1:]:
            return 0, None
        else:
            print(results)
            return len(results), min(results)
    else:
        results.append(current)
        return amicable_chain_recursive(current, data, results)

def calc95():
    i = 0
    min_min = None
    len_max = 0
    limit = 1000000
    data = []
    while(i <= limit):
        print(i)
        len_, min_ = amicable_chain_recursive(start=i, data=data)
        data.append([len_, min_])
        if len_ > len_max:
            len_max = len_
            min_min = min_
            place = i
        i += 1
    return min_min, place


# timer_wrapper(test4, 150)
# print(timer_wrapper(amicable_chain_recursive, 1000000,[]))
# print(amicable_chain_recursive(14316,[]))

# runs in ~450 seconds, need some more optimization
print(timer_wrapper(calc95))
