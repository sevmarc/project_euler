""" Digit sum numbers
A number where one digit is the sum of the other digits is called a digit sum number or DS-number for short. For example, 352, 3003 and 32812 are DS-numbers.

We define S(n) to be the sum of all DS-numbers of n digits or less.

You are given S(3)=63270 and S(7)=85499991450.

Find S(2020). Give your answer modulo 10^16 (-> last 16 digits).
"""

from function_collection.main import timer_wrapper

def sum_digits(x: str):
    sum_ = 0
    for n in x:
        sum_ += int(n)
    return sum_

def check_DS(x: int) -> bool:
    x_str = str(x)
    for c, num in enumerate(str(x)):
        temp = x_str[0:c:]+x_str[c+1::]
        # print(c, sum_digits(temp))
        if int(x_str[c]) == sum_digits(temp):
            # print(x, c, temp, sum_digits(temp))
            return True
    return False


def solution(diglen: int) -> int:
    sum_ = 0
    lim_ = 10**diglen
    for i in range(lim_):
        if check_DS(i):
            sum_ += i
    print(str(diglen), sum_)
    return sum_


if __name__ == '__main__':
    vals = []
    for i in range(1, 11):
        vals.append(timer_wrapper(solution, i))
    # for i in range(1, 6):
    #     print(vals[i]/vals[i-1])

