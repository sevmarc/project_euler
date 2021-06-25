"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. 
In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
from function_collection import timer_wrapper


def is_bouncy(x: int):
    decreasing = increasing = False
    for count, num in enumerate(str(x)):
        if count == 0:
            continue
        pre = int(str(x)[count - 1])
        num_int = int(num)
        if pre > num_int:
            decreasing = True
        if num_int > pre:
            increasing = True
        if decreasing and increasing:
            return True
    return False

def calc112():
    percentage_goal = 0.99  # 99%
    # percentage_goal = 0.9  # 90% for test -> 21780 (works)
    percentage = 0
    sum = 0
    iter_ = 0
    while(percentage_goal > percentage):
        iter_ += 1
        if is_bouncy(iter_):
            sum += 1
        percentage = sum / iter_
    return iter_

print(timer_wrapper(calc112))