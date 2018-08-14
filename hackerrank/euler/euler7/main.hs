primes :: [Integer]
primes = 2: 3: sieve (tail primes) [5,7..]
 where 
  sieve (p:ps) xs = h ++ sieve ps [x | x <- t, x `rem` p /= 0]  
                  where (h,~(_:t)) = span (< p*p) xs

main :: IO ()
main = do
    t <- readLn
    go t
    where
      go t
        | t < 1 = do return ()
        | otherwise = do
            n <- readLn
            print $ primes !! (n - 1)
            go (t - 1)
