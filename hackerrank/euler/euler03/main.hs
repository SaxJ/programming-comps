largestFactor :: Integer -> Integer
largestFactor n =
    maximum $ factor n

factor 1 = []
factor n = let divisors = dropWhile ((/= 0) . mod n) [2 .. ceiling $ sqrt $ fromIntegral n]
           in let prime = if null divisors then n else head divisors
              in (prime :) $ factor $ div n prime

main :: IO ()
main = do
    t <- readLn
    go t
    where
      go n
        | n < 1 = do return ()
        | otherwise = do
            x <- readLn
            print $ largestFactor x
            go (n-1)
