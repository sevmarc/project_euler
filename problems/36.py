def palindrome(w: str):
    if len(w) <= 1:
        return True
    if w[0] == w[len(w)-1]:
        if len(w) == 2:
            return True
        w1 = w[1:(len(w)-1)]
        # print(w, ' -> ', w1)
        return palindrome(w1)
    return False

print(palindrome("12321"))
print(palindrome("12311121"))
print(palindrome("12322221"))
print(palindrome("123321"))


maxval = 1000000

sum = 0
for i in range(1, maxval):
    if palindrome(str(i)) and palindrome(bin(i)[2:]):
        print(i, ' == ', bin(i))
        sum += i

print("SUM: ", sum)