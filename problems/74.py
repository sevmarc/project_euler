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

from function_collection.main import timer_wrapper
from function_collection.main import fact_recursive


factor_dict = {str(i): fact_recursive(i) for i in range(10)}


def sum_factor_digits_calc(x: int) -> int:
    return sum([fact_recursive(int(num_)) for num_ in str(x)])


def sum_factor_digits_lookup(x: int) -> int:
    return sum([factor_dict[num_] for num_ in str(x)])


def timer_test1() -> None:
    [sum_factor_digits_calc(i) for i in range(1000000)]


def timer_test2() -> None:
    [sum_factor_digits_lookup(i) for i in range(1000000)]


def cycle_of_factorials(start: int, acc=None) -> int:
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


def calc74(limit_: int = 1000000, goal_len: int = 60) -> int:
    return len([1 for i in range(limit_ + 1) if cycle_of_factorials(i) == goal_len])


if __name__ == '__main__':
    testing = False

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
        print(timer_wrapper(calc74))  # ~15 sec
