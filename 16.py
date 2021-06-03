from math import sqrt

def powdig(x,y):
    val = pow(x,y)
    sum = 0
    for w in str(val):
        sum += int(w)
    return sum

print(powdig(2, 15))
print(powdig(2, 1000))
