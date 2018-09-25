import Control.Monad

main :: IO ()
main = do
    cases <- readLn
    replicateM_ cases testCase

testCase :: IO ()
testCase = do
    n <- readLn
    print $ compute n

compute :: Integer -> Integer
compute n =
    let
        fac = product [1..n]
    in
        sum [read [x] | x <- show fac]
