# Triangular, pentagonal, and hexagonal

l = 100000
def triangle(limit=l):
    lst = []
    for i in range(1, limit):
        lst.append(int(i * (i + 1) / 2))
    return lst

def pentagonal(limit=l):
    lst = []
    for i in range(1, limit):
        lst.append(int(i * (3 * i - 1) / 2))
    return lst

def hexagonal(limit=l):
    lst = []
    for i in range(1, limit):
        lst.append(int(i * (2 * i - 1)))
    return lst

t = triangle()
p = pentagonal()
h = hexagonal()

for tn in t:
    if tn in p and tn in h:
        print("FOUND: ", tn)
