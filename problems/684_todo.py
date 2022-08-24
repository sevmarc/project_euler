""" Inverse Digit Sum
https://projecteuler.net/problem=684
"""

from math import pow
from function_collection.main import timer_wrapper


code_ = tuple[str, str]

fibarray = [0, 1]

def fibonacci(n: int) -> int:
    if n <= len(fibarray):  # Check is n is less than len(fibarray)
        return fibarray[n - 1]
    temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
    fibarray.append(temp_fib)
    return temp_fib


def add_digits(num: int) -> int:
    return sum([int(w) for w in str(num)])

def code_smallest_num(summa: int) -> code_:
    return str(summa % 9), str(int(summa / 9))

def decode_smallest_num(code_: code_) -> int:
    return int(code_[0] + '9' * code_[1])

def find_smallest_num(summa: int) -> int:
    return int(str(summa % 9) + ('9' * int(summa / 9)))


def sum_smallest_nums(n: int) -> int:
    return sum([find_smallest_num(i) for i in range(1, n + 1)])


def sum_fibos_mod(x: int) -> int:
    return sum([sum_smallest_nums(fibonacci(i)) for i in range(2, x)]) % 1000000007


def debug(n: int) -> list[int]:
    return [find_smallest_num(i) for i in range(1, n)]


if __name__ == '__main__':
    testing = True

    if testing:
        print(f"{fibonacci(100) = }")
        print(f"{sum_smallest_nums(20) = }")
        # timer_wrapper(print, f"{find_smallest_num2(100000) = }")
        timer_wrapper(print, f"{find_smallest_num(100000) = }")
        
        # print(f"{debug(fibonacci(90)) = }")
        print(f"{find_smallest_num(13) = }")

        # print(f"{sum_smallest_nums2(fibonacci(90)) = }")
        # print(f"{summing_debug(fibonacci(90)) = }")
        timer_wrapper(sum_smallest_nums, 20)
        