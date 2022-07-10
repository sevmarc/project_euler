""" Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000.
Find the product abc.
"""

def check_pyt(a: int, b: int, c: int) -> bool:
    return a*a + b*b == c*c

"""
# test
print(check_pyt(1,2,3))
print(check_pyt(3,4,5))
"""

if __name__ == '__main__':
    max_ = 998
    for a in range(1, max_):
        for b in range(1, max_ - a):
            c = 1000 - a - b
            if check_pyt(a,b,c):
                print(a, b, c, a*b*c)
                exit()
