""" 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

from function_collection import is_prime


if __name__ == '__main__':
    count = i = 0
    while (count < 10001):
        i += 1
        if is_prime(i):
            count += 1
    print(i)
