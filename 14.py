def collatz_len(n, counter=0):
    counter += 1
    if (n == 1):
        return counter
    if (n % 2) == 0:
        return collatz_len(int(n / 2), counter)
    else:
        return collatz_len(3 * n + 1, counter)

full = 1000000
max = 0
max_place = 0
for i in range(1, full):
    cur = collatz_len(i)
    if cur > max:
        max = cur
        max_place = i

print(max_place, max)

# print(ans_path[0], ans)