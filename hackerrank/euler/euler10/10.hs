-- Enter your code here. Read input from STDIN. Print output to STDOUT
import Data.List
import qualified Data.Map as M
import Data.Array.Unboxed

getInt :: IO (Int)
getInt = readLn

primeFactors n = factor n primes
  where
    factor n (p:ps) 
        | p*p > n        = [n]
        | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
        | otherwise      =     factor n ps
    
primes' :: [Int]
primes' = mkPrimes 2 M.empty
  where
    mkPrimes n m = case (M.null m, M.findMin m) of
        (False, (n', skips)) | n == n' ->
            mkPrimes (succ n) (addSkips n (M.deleteMin m) skips)
        _ -> n : mkPrimes (succ n) (addSkip n m n)
    addSkip n m s = M.alter (Just . maybe [s] (s:)) (n+s) m
    addSkips = foldl' . addSkip

primesSAE = 2 : sieve 3 4 (tail primesSAE) (inits primesSAE)
  where
  sieve x q ps (fs:ft) = [i | (i,True) <- assocs (
         accumArray (\ _ _ -> False)
                    True  (x,q-1)
                    [(i,()) | p <- fs, let c = p * div (x+p-1) p,
                              i <- [c, c+p..q-1]] :: UArray Int Bool )]
        ++ sieve q (head ps^2) (tail ps) ft
    
primes = 2 : filter (null . tail . primeFactors) [3,5..]
    
process :: Int -> IO ()
process n
    | n > 0 = do
        l <- getInt
        print $ sum $ takeWhile ( <= l) primesSAE
        process (n-1)
    | otherwise = return ()
    
main = do
    t <- getInt
    process t
