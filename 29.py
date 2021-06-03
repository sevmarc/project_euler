from math import pow

pows = []
n = 100
for a in range(2,n+1):
    for b in range(2,n+1):
        pows.append(pow(a,b))
print(len(set(pows)))