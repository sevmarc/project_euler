# Non-abundant sums
from function_collection.main import timer_wrapper
from function_collection.main import proper_divisors_fast


def deficient(x: int) -> bool:
    return x > sum(proper_divisors_fast(x))


def abundant(x: int) -> bool:
    return x < sum(proper_divisors_fast(x))


def perfect(x: int) -> bool:
    return x == sum(proper_divisors_fast(x))


def check_abundant_sum(x, ab: list[int]) -> bool:
    values = [i for i in ab if i < x]
    for v in values:
        if (x - v) in ab:
            # print(v, x-v)  # for actual results
            return True
    return False


def checker(ab: list[str]) -> int:
    return sum([i for i in range(1, limit) if not check_abundant_sum(i, ab)])


if __name__ == '__main__':
    testing = False

    limit = 28123
    abundants = [i for i in range(1, limit + 1) if abundant(i)]

    if testing:
        print(len(abundants))
        print(check_abundant_sum(24, abundants))
        print(check_abundant_sum(25, abundants))
        print(check_abundant_sum(23, abundants))
    else:
        print(timer_wrapper(checker, abundants))
