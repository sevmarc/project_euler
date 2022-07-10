""" (prime-k) factorial
For a prime p let S(p) = (∑ (p-k)!) mod(p) for 1 ≤ k ≤ 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that ∑ S(p) = 480 for 5 ≤ p < 100.

Find ∑ S(p) for 5 ≤ p < 10^8.
"""

from function_collection.main import is_prime, timer_wrapper

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def addition(i):
    return(fact(i-1) + \
           fact(i-2) + \
           fact(i-3) + \
           fact(i-4) + \
           fact(i-5)) % i

def solution():
    l = []
    lim_ = int(1e4)
    for i in range(5, lim_):
        if is_prime(i):
            l.append(addition(i))

    print(sum(l))


if __name__ == '__main__':
    timer_wrapper(solution)
