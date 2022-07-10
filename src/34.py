def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n - 1)

def digfact(x: int):
    w = str(x)
    sum = 0
    for l in w:
        sum += fact(int(l))
    return sum == x

print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))

low = 10
high = 100000

results = []
for i in range(low, high):
    if digfact(i):
        results.append(i)

print(results, sum(results))
