import collections
import time

def square_digits(n:int):
    lst = [(int(i))**2 for i in str(n)]
    return sum(lst)

def iterate(init:int):
    while(1):
        init = square_digits(init)
        if init == 1 or init == 89:
            return init

def counter(limit):
    count = 0
    pairs = {}
    for i in range(1, limit):
        print(i, count)
        if i in pairs:
            it = pairs[i]
        else:
            it = iterate(i)
            pairs.update({i: it})
        if it == 89:
            count += 1
    print(count)

start_time = time.time()

counter(10000000)
# can be greatly optimized

print(time.time() - start_time)
