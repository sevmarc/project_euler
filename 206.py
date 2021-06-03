import time
from math import sqrt
from itertools import permutations


# unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0
#     1_2_3_4_5_6_7_8_9_0
min = 1020304050607080900
max = 1929394959697989990
init_num = int(sqrt(min))
end_num = int(sqrt(max)) + 1


def word_permutations(x):
    words = []
    for w in list(permutations(str(x))):
        cur = ''
        for l in w:
            cur += l
        words.append(cur)
    return words


def fast_method():
    for i in range(10):
        pass


def try_square(x):
    sq = str(x * x)
    for l in range(0, 19, 2):
        if sq[l] != str((l / 2 + 1) % 10):
            return False
    return True


def iterate_check(start, end):
    for i in range(start, end):
        print(i, end - i)
        if try_square(i):
            print(i)
            return None
    return None


start_time = time.time()

# iterate_check(init_num, end_num)  # too slow
print(len(word_permutations("0123456789")))


print(time.time() - start_time)
