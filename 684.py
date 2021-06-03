from math import pow
import time


"""
def fibo_generator():
    a = 0
    b = 1
    while True:
        yield a
for index, number in enumerate(fibo()):
    if index == 100:
        print(index, number)
        break
"""

FibArray = [0, 1]


def fibonacci(n: int) -> int:
    if n <= 0:
        print("Incorrect input")
    # Check is n is less than len(FibArray)
    elif n <= len(FibArray):
        return FibArray[n - 1]
    temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
    FibArray.append(temp_fib)
    return temp_fib


def add_digits(num: int) -> int:
    return sum([int(w) for w in str(num)])


def find_smallest_num(summa: int) -> int:
    i = int(pow(10, summa / 9 - 1))
    while 1:
        if add_digits(i) == summa:
            return i
        i += 1


def find_smallest_num2(summa: int) -> int:
    if summa > 9:
        return int(str(find_smallest_num2(summa - 9)) + '9')
    else:
        return summa


def find_smallest_num3(summa: int) -> int:
    return int(str(summa % 9) + ('9' * int(summa / 9)))
    if summa > 9:
        return int(str(find_smallest_num2(summa - 9)) + '9')
    else:
        return summa


def sum_smallest_nums(n: int) -> int:
    return sum([find_smallest_num(i) for i in range(1, n+1)])


def sum_smallest_nums2(n: int) -> int:
    return sum([find_smallest_num2(i) for i in range(1, n+1)])


def sum_smallest_nums3(n: int) -> int:
    return sum([find_smallest_num3(i) for i in range(1, n+1)])


def summing_debug(n: int):
    sum = 0
    for i in range(1, n + 1):
        print(i)
        sum += find_smallest_num3(i)
    return sum


def sum_fibos_mod3(x: int) -> int:
    return sum([sum_smallest_nums3(fibonacci(i)) for i in range(2, x)]) % 1000000007


def sum_fibos_mod2(x: int) -> int:
    return sum([sum_smallest_nums2(fibonacci(i)) for i in range(2, x)]) % 1000000007


def debug(n: int):
    result = []
    for i in range(1, n):
        print(n-i)
        result.append(find_smallest_num3(i))
    return result


start_time = time.time()

# print(fibonacci(100))
# print(sum_smallest_nums(20))
# print(find_smallest_num2(10000))
# print(find_smallest_num3(10000))


# print(sum_fibos_mod2(12))
# print(time.time() - start_time)
# start_time = time.time()

print(debug(fibonacci(90)))
# print(find_smallest_num2(13))

# print(sum_smallest_nums2(fibonacci(90)))
# print(summing_debug(fibonacci(90)))

print(time.time() - start_time)
