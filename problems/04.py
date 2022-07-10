""" Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from function_collection.main import is_palindrome

def pal():
    return max(i*j for i in range(100,999) for j in range(100,999) if is_palindrome(i*j))
    
if __name__ == '__main__':
    print(pal())