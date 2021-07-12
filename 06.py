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

def sum_square(n: list[int]) -> int:
    sum = 0
    for i in n:
        sum += i * i
    return sum

def square_sum(m: list[int]) -> int:
    sum = 0
    for i in m:
        sum += i
    return sum * sum

"""
example_l = range(1,11)
print(sum_square(example_l))
print(square_sum(example_l))
print(square_sum(example_l) - sum_square(example_l))
"""

if __name__ == '__main__':        
    numlist = range(1,101)
    sum_of_squares = sum_square(numlist)
    square_of_sums = square_sum(numlist)
    print(square_of_sums - sum_of_squares)
