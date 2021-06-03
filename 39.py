perimeter = 120
# Integer right triangles

def pyth(a, b, c):
    s = sorted([a, b, c])
    a, b, c = s[0], s[1], s[2]
    return a*a + b*b == c*c

def perims(p):
    options = []
    for i in range(1, p):
        for j in range(1, p):
            if (i + j) < p:
                if pyth(i, j, p - i - j):
                    options.append(sorted([i, j, p - i - j]))

    return setter(options)

def setter(l):
    cur = []
    for i in l:
        if i not in cur:
            cur.append(i)
    return cur

print(perims(perimeter))


counter = 0

p = 1000
max = 0
for i in range(p):
    cur = perims(i)
    if len(cur) > max:
        max = len(cur)
        place = i
print("Result: ", place, " : ", max)