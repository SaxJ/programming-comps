module Lib
    ( process
    ) where

import Control.Monad

process :: IO ()
process = do
    n <- readLn
    replicateM_ n testCase
    where
        testCase = do
            i <- readLn
            print $ calculate i

calculate :: Int -> Int
calculate n = threes + fives - fifteens
    where
        t = (n - 1) `div` 3
        f = (n - 1) `div` 5
        c = (n - 1) `div` 15
        threes = 3 * t * (t + 1) `div` 2
        fives = 5 * f * (f + 1) `div` 2
        fifteens = 15 * c * (c + 1) `div` 2
