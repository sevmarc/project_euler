# Pandigital multiples
from collections import Counter

digits = "123456789"
explen = 9

def pandigital(w):
    if len(w) != 9:
        return False
    for i,j in Counter(w).items():
        if j != 1 or i not in digits:
            return False
    return True

# test
# print(pandigital("192384576"))
# print(pandigital("192"))
# print(pandigital("1923831"))

results = []
for i in range(1, 10000):
    for j in range(len(digits) + 1):
    # for j in range(len(str(i))):
        concat = ''
        for l in digits[:j]:
            concat += str(i * int(l))
        # print(concat)
        if pandigital(concat):
            print('num: ', i, ', digits: ', j)
            results.append(concat)

print(results)
print('MAX: ', max(results))
