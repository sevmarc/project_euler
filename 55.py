# Lychrel numbers
import time

def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

def check_lychrel(x, counter=0):
    count = counter
    new_x = x + int(str(x)[::-1])
    count += 1
    if is_palindrome(new_x):
        # print(count)
        return True
    elif counter < 50:
        return check_lychrel(new_x, count)
    else:
        return False

def count_lychrel_in_range(n):
    return len([i for i in range(n) if not check_lychrel(i)])

start_time = time.time()

print(count_lychrel_in_range(10000))

print(time.time() - start_time)