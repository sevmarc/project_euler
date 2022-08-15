
""" Coded triangle numbers
The nth term of the sequence of triangle numbers 
is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to 
its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle words?
"""

import string
from function_collection.utils import handle_filepath


def get_words() -> list[str]:
    f_words = open(handle_filepath("inputfiles/42.txt"), "r")
    wordlist = []
    for w in f_words:
        for a in (w.split('","')):
            a = a.replace('"', '')
            wordlist.append(a)
    return wordlist


def triangles(limit: int) -> list[int]:
    return [int(1/2 * i * (i + 1)) for i in range(1, limit)]


def ascii_conv(w: string) -> int:
    return sum([string.ascii_lowercase.index(l.lower()) + 1 for l in w])


def calc42() -> int:
    triangles_10000 = triangles(10000)
    words = get_words()
    return len([i for i in words if ascii_conv(i) in triangles_10000])


if __name__ == '__main__':
    testing = False

    if testing:
        print(f"{ascii_conv('SKY') == 55}")
    else:
        print(calc42())
