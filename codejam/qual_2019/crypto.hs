import Control.Monad
import Data.List
import qualified Data.Map.Strict as M
import Text.Printf

getInt :: IO (Int)
getInt = readLn

readInts :: String -> [Integer]
readInts s = [read x | x <- words s]

decompose :: [Integer] -> [Integer]
decompose (a:b:ls)
    | a == b = decompose (b:ls)
    | otherwise = (gcd a b) : decompose (b:ls)
decompose _ = []

makeChrMap :: [Integer] -> M.Map Integer Char
makeChrMap primes = M.fromList $ zip prs ['A'..'Z']
    where
        prs = nub $ sort primes

decode :: M.Map Integer Char -> [Integer] -> String
decode mp primes = map ((flip $ M.findWithDefault 'Z') mp) primes

testCase :: Int -> IO ()
testCase testN = do
    _ <- getLine
    cypherString <- getLine
    let cypher = readInts cypherString
    let primesFound' = decompose cypher

    let primesFound = (((head cypher) `div` (head primesFound')) : primesFound') ++ [(last cypher) `div` (last primesFound')]
    putStrLn $ printf "Case #%d: %s" testN $ decode (makeChrMap primesFound) primesFound

main :: IO ()
main = do
    t <- getInt
    mapM_ testCase [1..t]
