""" Prime pair sets
The primes 3, 7, 109, and 673, are quite remarkable. By taking 
any two primes and concatenating them in any order the result 
will always be prime. For example, taking 7 and 109, both 7109 
and 1097 are prime. The sum of these four primes, 792, represents 
the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two 
primes concatenate to produce another prime.
"""

from itertools import chain, combinations
from typing import Iterable, Iterator
from function_collection.main import is_prime, generate_primes
from function_collection.main import timer_wrapper


def powerset(iterable: Iterable) -> Iterator:
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def create_subset(l: list[int], n: int) -> list[chain[tuple[int]]]:
    return [i for i in powerset(l) if len(i) == n]


def concat_primes(ab: list[int]) -> bool:
    a, b = ab
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


def lookup() -> None:
    allprimes = generate_primes(1000)
    combo_5_primes = create_subset(allprimes, 4)
    for options in combo_5_primes:
        every2 = create_subset(options, 2)
        checking = True
        for prime_pairs in every2:
            checking = concat_primes(prime_pairs) and checking
        if checking:
            print("FOUND: ", every2)
            break


def lookup2() -> None:
    allprimes = generate_primes(10000)
    for p1 in allprimes:
        for p2 in allprimes:
            if concat_primes([p1, p2]):
                for p3 in allprimes:
                    if concat_primes([p1, p3]) and concat_primes([p2, p3]):
                        for p4 in allprimes:
                            if concat_primes([p1, p4]) and concat_primes([p2, p4]) and concat_primes([p3, p4]):
                                for p5 in allprimes:
                                    if concat_primes([p1, p5]) and concat_primes([p2, p5]) and concat_primes([p3, p5]) and concat_primes([p4, p5]):
                                        print("FOUND: ", p1, p2, p3, p4, p5)
                                        print("SUM", p1+p2+p3+p4+p5)
                                        return


if __name__ == '__main__':
    timer_wrapper(lookup2)
