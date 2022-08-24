""" Number Splitting
We define an S-number to be a natural number, n, that is a perfect square and its square root can be obtained by splitting the decimal representation of n into 2 or more numbers then adding the numbers.

For example, 81 is an S-number because sqrt(81) = 8 + 1.
6724 is an S-number: sqrt(6724) = 6 + 72 + 4.
8281 is an S-number: sqrt(8281) = 8 + 2 .
9801 is an S-number: .

Further we define T(N) to be the sum of all S numbers n <= N. You are given T(10^4) = 41333.

Find T(10^12) """


from function_collection.main import timer_wrapper
from math import sqrt


def generate_all_char_combinations(x: int, acc = []) -> list[list[int]]:
    """ 
    6724
    6 7 2 4
    6 72 4
    6 724
    67 2 4
    67 24
    672 4
    """
    ch = str(x)
    pos = acc
    if len(str(x)) == 2:
        return pos  # [ch[0], ch[1]]
    for i in range(1, len(ch)):
        a = ch[:i]
        b = ch[i:]
        print(f"{i = }: {a = }, {b = }")
        pos.append([a, generate_all_char_combinations(int(b))])
    return pos


def add_digits_all_combination(x: int) -> int:
    return sum([int(ch) for ch in str(x)])


def s_check(x: int) -> bool:
    """ x is expected to be a square number """
    return int(sqrt(x)) in list(set(map(sum, generate_all_char_combinations)))


if __name__ == '__main__':
    testing = True
    
    if testing:
        # print(generate_all_char_combinations(672))
        a = generate_all_char_combinations(6724)
        # print(generate_all_char_combinations(67245))
        print(f"{len(a) = }")
        for i in generate_all_char_combinations(6724):
            print(i)
        
    else:
        pass