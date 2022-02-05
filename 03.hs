{- Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
-}

-- factors :: Integer -> [Integer]
-- factors n = [toInteger x | x <- [2.. round . sqrt . fromIntegral n + 1], n `mod` fromIntegral x == 0]

sqrtRounded :: Int -> Int
sqrtRounded n = floor ( sqrt (fromIntegral  n) ) + 1

factors :: Int -> [Int]
factors n = [x | x <- [2..sqrtRounded n], n `mod` x == 0]

-- factorsRec :: Int -> Int -> [Int]
-- recursive factoring, divide by divisor, repeat
-- factorsRec n d = if n % 

isPrime :: Int -> Bool
isPrime n = null $ factors n

primeDivisors :: Int -> [Int]
primeDivisors n = [x | x <- [2..sqrtRounded n], isPrime x && n `mod` x == 0]

-- primeDivisors :: Integer -> [Integer]
-- primeDivisors n = [toInteger x | x <- [2..round . sqrt . fromIntegral n + 1], isPrime x & n `mod` fromIntegral x == 0]


calc = maximum $ primeDivisors 600851475143