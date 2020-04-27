module Main where

import Control.Monad
import Data.List

isPrime :: Integer -> Bool
isPrime n = (length [x | x <- [2 .. (sqrt $ ((fromIntegral n) :: Double))], mod n (floor x) == 0]) == 0

getInt :: IO Int
getInt = do
  line <- getLine
  return (read line :: Int)

testCase :: IO ()
testCase = do
  _ <- getInt
  numsLine <- getLine
  let nums = [read x :: Integer | x <- words numsLine]
  --let result = length $ goodSequences nums
  let result = length $ filter checkSquare $ sublists nums
  print result

sublists :: (Eq a) => [a] -> [[a]]
sublists = nub . concatMap tails . inits

factors :: Integer -> [Integer]
factors n = [x | x <- [1..n], n `mod` x == 0]

pairs :: (Eq a) => [a] -> [(a, a)]
pairs ns = [(a, b) | a <- ns, b <- ns]

checkSquare :: Integer -> Integer -> Bool
checkSquare x y = let
  q = (x - y) `div` 2
  p = (y + x) `div` 2
  in
    (p + q) * (p - q) == x * y
    

fast :: [Integer] -> Integer
fast nums = foldl check (1, 0) nums
  where
    check acc next = 

goodSequences :: [Integer] -> [[Integer]]
goodSequences nums = filter (\ns -> productIsSquare ns && (not . null) ns)$ sublists nums
  where
    isSquare n = any (\(a, b) -> (a - b) `mod` 2 == 0 && a * b == n) factorPairs
      where
        factorPairs = pairs $ factors n
    productIsSquare ns = isSquare $ product ns

doSquareSubseq :: IO ()
doSquareSubseq = do
  tests <- getInt
  replicateM_ tests testCase

main :: IO ()
main = do
  doSquareSubseq
