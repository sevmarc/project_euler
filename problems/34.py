""" Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from function_collection.main import fact_recursive


def digfact(x: int) -> bool:
    return x == sum([fact_recursive(int(l)) for l in str(x)])


def calc34():
    low = 10
    high = 100000

    results = [i for i in range(low, high) if digfact(i)]
    print(f"{results = }, {sum(results) = }")

if __name__ == '__main__':
    calc34()
