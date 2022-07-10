from math import pow

def checksum(x: int, n: int):
    sum = 0
    for l in str(x):
        sum += pow(int(l), n)
    return x == sum

"""
# test
print(checksum(1634, 4))
print(checksum(8208, 4))
print(checksum(9474, 4))
"""

max = 10000000
power = 5

sum = 0
for i in range(2, max):
    if checksum(i, power):
        print(i, " found!")
        sum += i
print("Result: ", sum)