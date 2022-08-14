""" Double-base palindromes
The decimal number, 585 = 10010010012 (binary), 
is palindromic in both bases.

Find the sum of all numbers, less than one million, 
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, 
in either base, may not include leading zeros.)
"""

from function_collection.main import is_palindrome


if __name__ == '__main__':
    maxval = 1000000
    result = sum([i for i in range(1, maxval) if is_palindrome(i)
                 and is_palindrome(int(bin(i)[2:]))])
    print(f"{result = }")
