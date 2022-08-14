""" Sum square difference
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 +...+ 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 +...+ 10)^2 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
"""

def sum_square(n: int) -> int:
    return sum([i * i for i in range(n + 1)])
    
def square_sum(m: int) -> int:
    return sum(range(m + 1)) ** 2


if __name__ == '__main__':       
    lim = 100
    print(square_sum(lim) - sum_square(lim))
