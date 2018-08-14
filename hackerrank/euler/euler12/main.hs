-- Enter your code here. Read input from STDIN. Print output to STDOUT
import Data.List
import qualified Data.Set as S

getInt :: IO Int
getInt = readLn

triangle :: Int -> Int
triangle n = (n * (n + 1)) `div` 2

triangles :: [Int]
triangles =  [triangle x | x <- [1..]]

primes = 2 : filter (null . tail . primeFactors) [3,5..]

primeFactors n = factor n primes
  where
    factor n (p:ps) 
        | p*p > n        = [n]
        | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
        | otherwise      =     factor n ps
     
nDivisors n = if n == 1 then 1 else product $ map ((+1) . length) (group (primeFactors n)) 
    
solve n = head $ filter ((> n) . nDivisors) triangles
    
main = do
    nTests <- getInt
    loop nTests
    where
        loop t
            | t > 0 = do
                n <- getInt
                --putStrLn $ show $ nDivisors 1
                putStrLn $ show $ solve n
                loop (t-1)
            | otherwise = do return ()
