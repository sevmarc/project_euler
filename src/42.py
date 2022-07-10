# 42.txt
import string

f_words = open("inputfiles/42.txt", "r")
wordlist = []
for w in f_words:
    for a in (w.split('","')):
        a = a.replace('"','')
        wordlist.append(a)
# print(wordlist)

def check_triangle(x: int):
    pass

def triangles(limit: int):
    tri = []
    for i in range(1, limit):
        tri.append(int(1/2 * i * (i + 1)))
    return tri

vals = triangles(10000)
print(vals)

counter = 0

def ascii_conv(w: string):
    s = 0
    for l in w:
        s += string.ascii_lowercase.index(l.lower()) + 1
    return s

print(ascii_conv("SKY"))

for s in wordlist:
    # print(s)
    if ascii_conv(s) in vals:
        counter += 1

print("FOUND: ", counter)