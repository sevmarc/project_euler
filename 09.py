# a + b + c = 1000
# a2 + b2 = c2

def check_pyt(a, b, c):
    return a*a + b*b == c*c
# test
"""
print(check_pyt(1,2,3))
print(check_pyt(3,4,5))
"""

max = 998
for i in range(1,max):
    for j in range(1,max - i):
        z = 1000 - i - j
        if check_pyt(i,j,z):
            print(i, j, z, i*j*z)