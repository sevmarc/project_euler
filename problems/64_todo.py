""" Odd period square roots

"""

from math import sqrt


def expand_sqrt(X: int):
    a0 = int(sqrt(X))
    repeating = []
    temp = int((sqrt(X) + a0) / (X - a0 ** 2))
    repeating.append(temp)
    for i in range(10):
        prev = repeating[i]
        if i > 1:
            prev_prev = repeating[i-1]
        else:
            prev_prev = a0
        mult = (X - prev_prev ** 2)
        temp = int(mult * (sqrt(X) + prev) / (X - prev ** 2))
        repeating.append(temp)
    return find_repeat_cycle(repeating), repeating


def find_repeat_cycle(values: list):
    cycle = None
    for i in range(1, len(values) - 1):
        looking = True
        for j in range(len(values) - i):
            if looking and values[j] == values[j + i]:
                cycle = i
            else:
                cycle = None
            if not cycle:
                looking = False
        if cycle:
            return cycle
    return None


if __name__ == '__main__':
    testing = True

    if testing:
        print(find_repeat_cycle([1, 2, 3, 4, 5, 1, 2, 3, 4]))
        print(find_repeat_cycle([1, 1, 1, 1]))
        print(find_repeat_cycle([1, 2, 1, 2]))
        print(find_repeat_cycle([1, 2, 1, 1]))
        print(find_repeat_cycle([1, 2, 2, 2]))
        print(find_repeat_cycle([1, 2, 3, 1, 2, 3, 1]))
    else:
        print(expand_sqrt(23))
