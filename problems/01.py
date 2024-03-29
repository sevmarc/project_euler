""" Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def mult_3_5(n: int):
    return sum([i for i in range(n) if (i % 3 == 0) or (i % 5 == 0)])

# print(mult_3_5(10))  # test


if __name__ == '__main__':
    print(mult_3_5(1000))
