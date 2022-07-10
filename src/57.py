# Square root convergents

"""
expansions:
3   /   2       1+  1/2
7   /   5           2/5
17  /   12          5/12
41  /   29          12/29
99  /   70          29/70
239 /   169         70/169
577 /   408         169/408
1393/   985         408/985
"""


def generate_exp(n: int):
    if n == 1:
        return [3, 2]
    else:
        a = generate_exp(n - 1)
        denum = a[1] + a[0]
        num = a[1] + denum
        return [num, denum]


def calc_larger_numerator(limit: int):
    lst = [generate_exp(i) for i in range(1, limit)]
    count = 0
    for i in range(1, limit + 1):
        current = generate_exp(i)
        if len(str(current[0])) > len(str(current[1])):
            count += 1
    print('found: ', count)


calc_larger_numerator(1000)
