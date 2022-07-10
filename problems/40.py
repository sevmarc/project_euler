# Champernowne's constant
# 0.123456789101112131415161718192021...
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000 = ?

maxval = 1000000
w = ''
for i in range(0,maxval):
    w += str(i)

"""
# test
print(w[12])
print(w[5])
"""
prod = 1
for n in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    prod *= int(w[n])
print("Result: ", prod
