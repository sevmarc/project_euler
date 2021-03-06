{- Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
-}

mult35 :: Int -> Bool
mult35 n = (n `mod` 3 == 0) || (n `mod` 5 == 0)

multlist :: [Int] -> [Int]
multlist (n : ns) = if mult35 n then n : multlist ns else multlist ns
multlist [] = []
    
calc :: Int
calc = sum $ multlist [1..999]
