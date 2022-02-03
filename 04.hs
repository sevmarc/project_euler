{- Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
-}


palindrome :: Int -> Bool
-- reverse the string then read it back
palindrome a = a == read (reverse (show a)) 

calc :: Int
calc = maximum [i * j | i <- [100..1000], j <- [100..1000], palindrome (i * j)]
