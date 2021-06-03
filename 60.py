from itertools import chain, combinations
from math import sqrt
import time

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def generate_primes(x):
    return [p for p in range(x) if is_prime(p)]

def create_subset(l, n):
    return [i for i in powerset(l) if len(i) == n]

def concat_primes(ab):
    a = ab[0]
    b = ab[1]
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


def lookup():
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

def lookup2():
    allprimes = generate_primes(10000)
    for p1 in allprimes:
        for p2 in allprimes:
            if concat_primes([p1,p2]):
                for p3 in allprimes:
                    if concat_primes([p1,p3]) and concat_primes([p2, p3]):
                        for p4 in allprimes:
                            if concat_primes([p1,p4]) and concat_primes([p2, p4]) and concat_primes([p3,p4]):
                                for p5 in allprimes:
                                    if concat_primes([p1,p5]) and concat_primes([p2, p5]) and concat_primes([p3,p5]) and concat_primes([p4, p5]):
                                        print("FOUND: ", p1, p2, p3, p4, p5)
                                        print("SUM", p1+p2+p3+p4+p5)
                                        return

start_time = time.time()

lookup2()

print(time.time() - start_time)