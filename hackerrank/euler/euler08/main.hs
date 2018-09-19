-- Enter your code here. Read input from STDIN. Print output to STDOUT
import System.IO
import Data.List
import Data.Char

getInt :: IO Int
getInt = readLn

maxProd :: (Num a, Ord a) => Int -> [a] -> a
maxProd n = maximum . map product . takeWhile ((== n) . length) . map (take n) . tails

processTests :: Int -> IO ()
processTests t
    | t > 0 = do
        line <- getLine
        let nums = [read w :: Int | w <- words line]
        test <- getLine
        let digits = [digitToInt d | d <- test]
        putStrLn $ show  $ maxProd (last nums) digits
        processTests (t -  1)
    | otherwise = do
        return ()
        

main = do
    n <- getInt
    processTests n
