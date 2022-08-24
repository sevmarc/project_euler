""" Powers of Two
2^7 = 128 is the first power of two whose leading digits are "12".
The next power of two whose leading digits are "12" is 2^80.

Define p(L, n) to be the nth-smallest value of j such that the base 10 representation of 2^j begins with the digits of L.
So p(12, 1) = 7 and p(12, 2) = 80.

You are also given that p(123, 45) = 12710.

Find p(123, 678910).
"""


from function_collection.main import exp_by_squaring, timer_wrapper


def second_powers(n: int):
    return [int(exp_by_squaring(2, i)) for i in range(1, n)]


def p(L: int, n: int) -> int:
    counter = num = 0

    while (True):
        sq = exp_by_squaring(2, num)
        if str(sq).startswith(str(L)):
            counter += 1
            if counter == n:
                return num
        num += 1


def test1() -> bool:
    return p(12, 1) == 7


def test2() -> bool:
    return p(12, 2) == 80


def test3() -> bool:
    return p(123, 45) == 12710


def calc686() -> int:
    return p(123, 678910)


if __name__ == '__main__':
    testing = False

    if testing:
        powers = timer_wrapper(second_powers, 26000)
        print(timer_wrapper(test1))
        print(timer_wrapper(test2))
        print(timer_wrapper(test3))
    else:
        result = timer_wrapper(calc686)
        print(f"{result = }")
