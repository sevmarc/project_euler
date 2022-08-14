"""
https://oeis.org/A051626
https://oeis.org/A051626/b051626.txt
"""

f_open = open("problems/inputfiles/26.txt", "r")
lines = {}
for line in f_open:
    line = line.split()
    lines.update({line[0]: line[1]})
# print(lines)

max = 0
place = 0
for j,k in lines.items():
    if int(k) > max:
        max = int(k)
        place = j
print(place, ': ', max)