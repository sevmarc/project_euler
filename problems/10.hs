{- Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
-}

sqrtRounded :: Int -> Int
sqrtRounded n = floor ( sqrt (fromIntegral  n) ) + 1

factors :: Int -> [Int]
factors n = [x | x <- [2..sqrtRounded n], n `mod` x == 0]

factorsRec :: Int -> Int -> [Int] -> [Int]
-- recursive factoring, divide by divisor, repeat
factorsRec n d divs
  | d == n = divs ++ [d]
  | n `mod` d == 0 = factorsRec (n `div` d) 2 divs ++ [d]
  | otherwise = factorsRec n (d + 1) divs

isPrime :: Int -> Bool
isPrime 2 = True
isPrime n = null $ factors n

isPrimeRec :: Int -> Bool
isPrimeRec 2 = True
isPrimeRec n = factorsRec n 1 [] == [1,n]

calc1 :: Int
calc1 = sum [i | i <- [1..2000000], isPrime i]

calc2 :: Int
calc2 = sum [i | i <- [1..2000000], isPrimeRec i]

calc = calc1