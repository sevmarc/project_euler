{- Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000.
Find the product abc.
-}

checkPyt :: Int -> Int -> Int -> Bool
checkPyt a b c = a*a + b*b == c*c

calc :: [Int]
calc = [i * j * (1000-i-j) | i <- [1..998], j <- [1..998-i], checkPyt i j (1000-i-j)]
-- k = 1000-i-j -> i+j+k = 1000