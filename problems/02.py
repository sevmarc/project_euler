""" Even Fibonacci numbers
Each new term in the Fibonacci sequence is generated by adding the 
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do
not exceed four million, find the sum of the even-valued terms.
"""


def fibo_rec(n: int) -> int:  # recursive
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_data(n: int, data: list[int]) -> int:  # recursive
    if len(data) >= 2:
        return data[-2] + data[-1]  # sum last two
    else:
        return fibo_rec(n)


def fibo_even_sum(limit_=4000000) -> int:
    sum_, cur = 0, 0
    x = 1
    data = []
    while (cur < limit_):
        cur = fibo_data(x, data)
        data.append(cur)
        if cur % 2 == 0:
            sum_ += cur
        x += 1
    return sum_


if __name__ == '__main__':
    print(fibo_even_sum())
