{- Sum square difference
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 +...+ 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 +...+ 10)^2 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025-385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
-}

sumSquare :: Int -> Int
sumSquare n = sum [i^2 | i <- [1..n]]

squareSum :: Int -> Int
squareSum n = sum [1..n] ^ 2

calc :: Int
calc =  squareSum 100 - sumSquare 100
