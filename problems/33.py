def curious_fraction(a: int, b: int):
    frac = a / b
    common = ''.join(set(str(a)).intersection(str(b)))
    print(f"common in {a}/{b}: {common}")
    for l in common:
        cur_a = str(a).replace(l, '')
        cur_b = str(b).replace(l, '')
        if len(cur_a) > 0 and len(cur_b) > 0 and cur_a != '0' and cur_b != '0':
            if (float(cur_a) / float(cur_b) == frac):
                return True
    return False

"""
# test
print(curious_fraction(49, 98))
print(curious_fraction(49, 41))
print(curious_fraction(30, 50))
"""

results = []
for i in range(1, 100):
    for j in range(1, 100):
        if i < j:
            if (i % 10 != 0) and (j % 10 != 0):
                if curious_fraction(i, j):
                    results.append([i, j])
print(results)

num = 1
denum = 1
for r in results:
    num *= r[0]
    denum *= r[1]
print(num, '/', denum)