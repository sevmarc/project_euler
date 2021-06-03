def check_pal(n: int):
    if str(n) == (str(n))[::-1]:
        return True
    else:
        return False
"""
print(check_pal(1111))
print(check_pal(1211))
print(check_pal(1221111))
print(check_pal(113311))
"""

def pal():
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            if check_pal(i*j):
                return i*j
    return None

print(pal())