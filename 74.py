""" Digit factorial chains
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with 
a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

from function_collection import timer_wrapper


def factor_rec(n: int) -> int:
    if n <= 1:
        return 1
    return n * factor_rec(n -1)

def sum_factor_digits_calc(x: int) -> int:
    sum_ = 0
    for num_ in str(x):
        sum_ += factor_rec(int(num_))
    return sum_

factor_dict = {}
for i in range(10):
    factor_dict.update( {str(i): factor_rec(i)} )

def sum_factor_digits_lookup(x: int) -> int:
    sum_ = 0
    for num_ in str(x):
        sum_ += factor_dict[num_]
    return sum_

def timer_test1():
    maxnum = 1000000
    for i in range(maxnum):
        sum_factor_digits_calc(i)

def timer_test2():
    maxnum = 1000000
    for i in range(maxnum):
        sum_factor_digits_lookup(i)


def cycle_of_factorials(start: int, acc=None):
    current = sum_factor_digits_lookup(start)

    if acc:
        results = acc
    else:
        results = [start]

    if current in results:  # or is_perfect(current) 
        return len(results)
    else:
        results.append(current)
    return cycle_of_factorials(current, results)

def calc74():
    i = 0
    goal_len = 60
    count = 0
    starter_limit = 1000000
    while(i <= starter_limit):
        len_ = cycle_of_factorials(i)
        if len_ == goal_len:
            count += 1
        i += 1
    return count

testing = False

if __name__ == '__main__':
    if testing:
        print(factor_dict)
        timer_wrapper(timer_test1)
        timer_wrapper(timer_test2)

        print(cycle_of_factorials(145, []))
        print(cycle_of_factorials(169, []))
        print(cycle_of_factorials(871, []))
        print(cycle_of_factorials(872, []))
        print(cycle_of_factorials(69, []))
        print(cycle_of_factorials(78, []))
        print(cycle_of_factorials(540, []))

    else:
        print(timer_wrapper(calc74))  # ~55 sec
