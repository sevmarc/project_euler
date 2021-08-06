""" Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from function_collection.main import unique_prime_divisors

if __name__ == '__main__':
    print(max(unique_prime_divisors(600851475143)))
