def sum_square(n: list):
    sum = 0
    for i in n:
        sum += i * i
    return sum

def square_sum(m: list):
    sum = 0
    for i in m:
        sum += i
    return sum * sum
"""
example_l = range(1,11)
print(sum_square(example_l))
print(square_sum(example_l))
print(square_sum(example_l) - sum_square(example_l))
"""
task_l = range(1,101)
ss1 = sum_square(task_l)
print(ss1)
ss2 = square_sum(task_l)
print(ss2)
print(ss2 - ss1)