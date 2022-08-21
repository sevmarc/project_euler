""" Square remainders
Let r be the remainder when (a-1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑rmax.
"""

from function_collection.main import exp_by_squaring, timer_wrapper


def square_remainders_rec(a: int, n: int) -> int:
    return (exp_by_squaring(a-1, n) + exp_by_squaring(a+1, n)) % (a**2)


def square_remainders(a: int, n: int) -> int:
    return ((a-1)**n + (a+1)**n) % (a**2)


def test() -> bool:
    return square_remainders(7, 3) == 42  # based on given example


def check_rmax(a: int, n_limit: int = 2000) -> int:
    # n_limit needs tuning, optimization
    return max([square_remainders(a, n) for n in range(1, n_limit)])


def summa_rmax() -> int:
    return sum(check_rmax(i) for i in range(3, 1001))


if __name__ == '__main__':
    testing = False

    if testing:
        print(test())
    else:
        result = timer_wrapper(summa_rmax)
        print(f"{result = }")
