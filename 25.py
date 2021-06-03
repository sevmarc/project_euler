from math import pow

"""
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# test
for i in range(1,15):
    print(i, ': ', fibo(i))


phi = 1.61803398875
arg = 100
calc = fibo(arg)
print(arg, ': ', calc)
for i in range(1,100000000):
    # print(i, ': ', fibo(i), fibo(10)*pow(phi, i-10))
    # print(i, ': ', fibo(10)*pow(phi, i-10))
    cur = calc*pow(phi, i-arg)
    if len(str(cur)) == 1000:
        print(i, ': ', cur)
        break
"""

def fibo():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

for index, number in enumerate(fibo()):
    if len(str(number)) == 1000:
        print(index)
        break
