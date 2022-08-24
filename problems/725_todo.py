""" Digit sum numbers
A number where one digit is the sum of the other digits is called a digit sum number or DS-number for short. For example, 352, 3003 and 32812 are DS-numbers.

We define S(n) to be the sum of all DS-numbers of n digits or less.

You are given S(3)=63270 and S(7)=85499991450.

Find S(2020). Give your answer modulo 10^16 (-> last 16 digits).
"""

from function_collection.main import timer_wrapper


def sum_digits(x: str, avoid_first_occurence: str = '') -> int:
    return sum(int(n) for n in x.replace(str(avoid_first_occurence), '', 1))


def largest_digit(x: str) -> int:
    return max(int(n) for n in x)


def check_ds(x: int) -> bool:
    """
    s = 2:
        i = 11
        i = 22
        i = 33
        i = 44
        i = 55
        i = 66
        i = 77
        i = 88
        i = 99
    """
    x_str = str(x)
    largest_digit_ = largest_digit(x_str)
    return largest_digit_ == sum_digits(x_str, avoid_first_occurence=str(largest_digit_))


def check_ds_2(x: int) -> bool:
    x_str = str(x)
    for c in range(len(x_str)):
        temp = x_str[0:c:]+x_str[c+1::]
        if int(x_str[c]) == sum_digits(temp):
            return True
    return False


def solution(diglen: int) -> int:
    """
    solution(1) = 0
    solution(2) = 495
    solution(3) = 63270
    solution(4) = 3149685
    solution(5) = 112398876
    solution(6) = 3311663355
    solution(7) = 85499991450
    solution(8) = 1998499980015
    """
    for i in range(10, 10 ** diglen):
        if check_ds(i):
            print(f"{i = }")
    return sum(i for i in range(10, 10**diglen) if check_ds(i))


def test1() -> bool:
    return solution(3) == 63270


def test2() -> bool:
    return solution(7) == 85499991450


if __name__ == '__main__':
    testing = True
    if testing:
        print(f"{timer_wrapper(test1) = }")
        print(f"{timer_wrapper(test2) = }")
    else:
        result = timer_wrapper(solution, 16)
        print(f"{result = }")
