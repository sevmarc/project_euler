""" Square digit chain
A number chain is created by continuously adding the square of the 
digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an 
endless loop. What is most amazing is that EVERY starting number will 
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

from function_collection.main import timer_wrapper


def square_digits(n: int) -> int:
    lst = [(int(i))**2 for i in str(n)]
    return sum(lst)


def iterate(init: int) -> int:
    while (1):
        init = square_digits(init)
        if init == 1 or init == 89:
            return init


def counter(limit: int) -> int:
    pairs = {i: iterate(i) for i in range(1, limit)}
    return len([i for i in list(pairs.values()) if i == 89])


if __name__ == '__main__':
    result = timer_wrapper(counter, 10000000)
    print(f"{result = }")
    # can be greatly optimized
