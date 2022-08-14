""" Pandigital multiples
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital,
192384576. We will call 192384576 the concatenated product 
of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying 
by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that 
can be formed as the concatenated product of an integer 
with (1,2, ... , n) where n > 1?
"""

from collections import Counter


digits = "123456789"
explen = 9


def pandigital(w: str) -> bool:
    if len(w) != 9:
        return False
    for i, j in Counter(w).items():
        if j != 1 or i not in digits:
            return False
    return True


def calc38(debug: bool = False) -> int:
    results = []
    for i in range(1, 10000):
        for j in range(len(digits) + 1):
            concat = ''.join([str(i * int(l)) for l in digits[:j]])
            if pandigital(concat):
                if debug:
                    print('num: ', i, ', digits: ', j)
                results.append(int(concat))
    return max(results)


if __name__ == '__main__':
    testing = False

    if testing:
        print(pandigital("192384576"))
        print(pandigital("192"))
        print(pandigital("1923831"))
    else:
        result = calc38()
        print(f"{result = }")
