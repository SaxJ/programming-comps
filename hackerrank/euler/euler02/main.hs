fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

sumEvens :: Integer -> Integer
sumEvens n = sum [x | x <- takeWhile (<= n) fibs, x `mod` 2 == 0]

process t
  | t < 1 = do return ()
  | otherwise = do
      n <- readLn
      print $  sumEvens n
      process (t-1)

main :: IO ()
main = do
    t <- readLn
    process t
