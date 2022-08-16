""" Self powers
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from function_collection.main import exp_by_squaring
from function_collection.main import timer_wrapper


def summa(iter: int = 1000) -> str:
    sum_of_powers = sum([int(exp_by_squaring(i, i))
                        for i in range(1, iter + 1)])
    return str(sum_of_powers)[-10:]


if __name__ == '__main__':
    result = timer_wrapper(summa)
    print(f"{result = }")
