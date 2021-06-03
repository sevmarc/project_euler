def mult_3_5(n: int):
    mult = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            mult += i
    return mult

print(mult_3_5(10))
print(mult_3_5(1000))