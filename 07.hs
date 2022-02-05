{- 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
-}

sqrtRounded :: Int -> Int
sqrtRounded n = floor ( sqrt (fromIntegral  n) ) + 1

factors :: Int -> [Int]
factors n = [x | x <- [2..sqrtRounded n], n `mod` x == 0]

-- factorsRec :: Int -> Int -> [Int]
-- recursive factoring, divide by divisor, repeat
-- factorsRec n d = if n % 

isPrime :: Int -> Bool
isPrime n = null $ factors n

nthPrime :: Int -> Int -> Int
-- the second argument is an accumulator
nthPrime 0 b = b - 1
nthPrime a b = if isPrime b 
               then nthPrime (a-1) (b+1) 
               else nthPrime a (b+1)

calc :: Int
calc = nthPrime (10001+1) 0
