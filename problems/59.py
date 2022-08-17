""" XOR decryption
Each character on a computer is assigned a unique code and the 
preferred standard is ASCII (American Standard Code for Information 
Interchange). For example, uppercase A = 65, asterisk (*) = 42, and 
lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to 
ASCII, then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption 
key on the cipher text, restores the plain text; for example, 65 XOR 42 
= 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain 
text message, and the key is made up of random bytes. The user would 
keep the encrypted message and the encryption key in different 
locations, and without both "halves", it is impossible to decrypt the 
message.

Unfortunately, this method is impractical for most users, so the 
modified method is to use a password as a key. If the password is 
shorter than the message, which is likely, the key is repeated 
cyclically throughout the message. The balance for this method is using 
a sufficiently long password key for security, but short enough to be 
memorable.

Your task has been made easy, as the encryption key consists of three 
lower case characters. Using p059_cipher.txt (right click and 'Save 
Link/Target As...'), a file containing the encrypted ASCII codes, and 
the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the 
original text.
"""

import time
import string
from function_collection.utils import handle_filepath
from function_collection.main import timer_wrapper

# the encryption key consists of three lower case characters


def read_message_from_file(file: str) -> list[str]:
    vals = [line.split(',') for line in open(file, 'r')][0]
    return [chr(int(val)) for val in vals]


def decode(message: str, key: str) -> list[str]:
    return [chr(ord(l) ^ ord(key[i % 3])) for i, l in enumerate(message)]


def check_for_words(word: str, min_nu_of_occurence: int, message: str) -> bool:
    count = 0
    for i, m in enumerate(message):
        notfound = True
        if m == word[0]:
            for j, l in enumerate(word):
                if message[i + j] != l:
                    notfound = False
            if notfound:
                count += 1
    if count >= min_nu_of_occurence:
        return True
    else:
        return False


def all_keys() -> list[str]:
    keys = []
    for l0 in list(string.ascii_lowercase):
        for l1 in list(string.ascii_lowercase):
            for l2 in list(string.ascii_lowercase):
                w = l0 + l1 + l2
                keys.append(w)
    return keys


def calc59(msg: str, keylist: list[str]) -> tuple[str, str, int]:
    for k in keylist:
        d = decode(msg, k)
        if check_for_words('the', 7, d):
            w = ''.join([l for l in d])
            sum_ = sum([ord(l) for l in d])
            return (w, k, sum_)


if __name__ == '__main__':
    msg = read_message_from_file(handle_filepath('inputfiles/59.txt'))
    keylist = all_keys()

    testing = False

    if testing:
        print(f"{msg = }")
        print(check_for_words('the', 2, "the man and the cow"))
    else:
        decoded_message, key_, sum_ = timer_wrapper(calc59, [msg, keylist])
        print(f"{decoded_message = }")
        print(f"{key_ = }")
        print(f"{sum_ = }")
