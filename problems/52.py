from collections import Counter

m = [1, 2, 3, 4, 5, 6]

# print(Counter("asd") == Counter("dsa"))
def compare_counters(lst):
    for ind in range(len(lst) - 1):
        if Counter(str(lst[ind])) != Counter(str(lst[ind + 1])):
            return False
    else:
        return True

maxval = 1000000
for i in range(10, maxval):
    cur = []
    for mult in m:
        cur.append(mult * i)
    if compare_counters(cur):
        print("BOOYAH! ", i, 2*i, 3*i, 4*i, 5*i, 6*i)