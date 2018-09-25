import Control.Monad
import Data.List
import qualified Data.Map.Strict as Map

main :: IO ()
main = do
    cases <- readLn
    replicateM_ cases testCase

testCase :: IO ()
testCase = do
    n <- readLn
    print $ calculate n

calculate :: Int -> Int
calculate n = sum . takeWhile (<= n) $ amicables

amicables :: [Int]
amicables = [220,284,1184,1210,2620,2924,5020,5564,6232,6368,10744,10856,12285,14595,17296,18416,63020,66928,66992,67095,69615,71145,76084,79750,87633,88730,100485,122265,122368,123152,124155,139815,141664,142310,153176,168730,171856,176272,176336,180848]
