def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_even_sum():
    sum = 0
    for i in range(1, 1000):
        cur = fibo(i)
        if cur % 2 == 0:
            sum += cur
        if cur > 4000000:
            return sum

for i in range(1,20):
    print(fibo(i))

print(fibo_even_sum())