""" Prime cube partnership
There are some prime values, p, for which there exists a positive integer, n, such that the expression n^3 + n^2p is a perfect cube.

For example, when p = 19, 8^3 + 8^2x19 = 12^3.

What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
"""

"""
we can rearrange n^3 + n^2 * p = n^2 * (n + p)
n^2 * (n + p) = x^3

"""

from function_collection.main import is_power


def check(x: int):
    pass