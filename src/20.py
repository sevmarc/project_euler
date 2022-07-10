def fact(x):
    if x == 1:
        return 1
    else:
        return (x) * fact(x-1)

def sumdigit(x):
    sum = 0
    for w in str(x):
        sum += int(w)
    return sum

print(sumdigit(fact(100)))