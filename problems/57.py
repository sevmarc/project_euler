""" Square root convergents

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


def generate_exp(n: int) -> list[int]:
    if n == 1:
        return [3, 2]
    else:
        a = generate_exp(n - 1)
        denum = a[1] + a[0]
        num = a[1] + denum
        return [num, denum]


def calc_larger_numerator(limit: int) -> int:
    larger_numerator = [generate_exp(i) for i in range(
        1, limit + 1) if len(str(generate_exp(i)[0])) > len(str(generate_exp(i)[1]))]
    return len(larger_numerator)


if __name__ == '__main__':
    result = calc_larger_numerator(1000)
    print(f"{result = }")
