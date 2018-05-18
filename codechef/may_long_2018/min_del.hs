import Data.Maybe

gcdSeq :: [Int] -> Maybe Int
gcdSeq [] = Nothing
gcdSeq [_] = Nothing
gcdSeq [x, y] = Just $ gcd x y
gcdSeq (x:xs) = Just $ gcd x $ fromJust $ gcdSeq xs

check :: [Int] -> [Int]
check [] = []
check [a] = [a]
check [a, b] = if gcd a b /= 1 then [a] else [a, b]
check (x:xs) = if gcd x (fromJust (gcdSeq xs)) /= 1 then xs else x:(check xs)

process :: Int -> [Int] -> Int
process size xs = let
    remaining = length $ check xs
    diff = size - remaining
    in
        if remaining == 1 then -1 else diff

testCase :: Int -> IO ()
testCase c
    | c > 0 = do
        size <- readLn
        numbers <- getLine
        print $ process size $ [read x | x <- words numbers]
        testCase (c - 1)
    | otherwise = return ()

main :: IO ()
main = do
        cases <- readLn
        testCase cases
