""" Longest Collatz sequence
The following iterative sequence is defined 
for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, 
we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and 
finishing at 1) contains 10 terms. Although it has not 
been proved yet (Collatz Problem), it is thought that 
all starting numbers finish at 1.

Which starting number, under one million, 
produces the longest chain?

NOTE: Once the chain starts the terms are 
allowed to go above one million.
"""

from function_collection import timer_wrapper

def collatz_len(n: int, counter:int=0) -> int:
    counter += 1
    if (n == 1):
        return counter
    if (n % 2) == 0:
        return collatz_len(int(n / 2), counter)
    else:
        return collatz_len(3 * n + 1, counter)

def calc14(full=1000000):
    max_ = 0
    max_place = 0
    for i in range(1, full):
        cur = collatz_len(i)
        if cur > max_:
            max_ = cur
            max_place = i
    print(max_place, max_)

    # print(ans_path[0], ans)

if __name__ == '__main__':
    timer_wrapper(calc14)
