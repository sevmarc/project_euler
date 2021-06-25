# XOR decryption
import time
import string

"""
print(ord('A'))
print(ord('k'))
print(ord('*'))
"""

# the encryption key consists of three lower case characters

def read_message_from_file(file):
    vals = [line.split(',') for line in open(file, 'r')][0]
    return [chr(int(val)) for val in vals]

def decode(message, key):
    decoded = []
    for i,l in enumerate(message):
        k = key[i % 3]
        decoded.append(chr(ord(l) ^ ord(k)))
    return decoded

def check_for_words(word, min_nu_of_occurence, message):
    count = 0
    for i,m in enumerate(message):
        notfound = True
        if m == word[0]:
            for j,l in enumerate(word):
                if message[i + j] != l:
                    notfound = False
            if notfound:
                count += 1
    if count >= min_nu_of_occurence:
        return True
    else:
        return False

def all_keys():
    keys = []
    for l0 in list(string.ascii_lowercase):
        for l1 in list(string.ascii_lowercase):
            for l2 in list(string.ascii_lowercase):
                w = l0 + l1 + l2
                keys.append(w)
    return keys


start_time = time.time()

msg = read_message_from_file('inputfiles/59.txt')
keylist = all_keys()
# print(msg)
# print(check_for_words('the', 2, "the man and the cow"))
for k in keylist:
    d = decode(msg, k)
    if check_for_words('the', 7, d):
        w = ''
        sum = 0
        for l in d:
            sum += ord(l)
            w += l
        print(w, k, sum)


print(time.time() - start_time)