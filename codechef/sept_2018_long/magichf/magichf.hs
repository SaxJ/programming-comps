import Control.Monad

main :: IO ()
main = do
    cases <- readLn
    replicateM_ cases testCase

testCase :: IO ()
testCase = do
    line <- getLine
    let [n, x, s] = [read x | x <- words line]
    pairs <- replicateM s getSwap
    putStrLn $ process pairs n x
    where
        getSwap = do
            ln <- getLine
            let [a, b] = [read x | x <- words ln]
            return (a, b)

process :: [(Int, Int)] -> Int -> Int -> String
process [] boxes coin = show coin
process ((a,b):ls) boxes coin
    | a == coin = process ls boxes b
    | b == coin = process ls boxes a
    | otherwise = process ls boxes coin
