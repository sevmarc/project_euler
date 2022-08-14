""" Anagramic squares
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""

from collections import Counter
from function_collection.main import is_square
from itertools import combinations


def load_words(filename: str):
    with open(filename, "r") as words:
        wordlist = []
        whole = words.readlines()[0]
        for w in whole.split(','):
            w_mid = w[1:(len(w)-1)]  # "..."
            wordlist.append(w_mid)
        return wordlist

def check_anagram(word1: str, word2: str) -> bool:
    return Counter(word1) == Counter(word2)

def check_squares(word1: str, word2: str) -> int:
    """
    input: 2 anagramms
    output: max square

    mazda, azdam
    map all character to a number:
        m, a, z, d -> 1, 2, 3, 4 etc.
    check if word is square, if not, continue, if it is, store max
    returns 0 if it is not squareable
    """
    char_len = len(Counter(word1).keys())
    first_chars = [word1[0], word2[0]]
    print(Counter(word1).keys())
    c = combinations(range(10), char_len)
    print(list(c))

if __name__ == '__main__':
    a= load_words('problems/inputfiles/98_words.txt')
    
    print(check_anagram("mazda","azmad"))
    print(check_anagram("mazda","azmad1"))
    check_squares("mazda", "azmad")